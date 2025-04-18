
from datetime import datetime, timedelta
import pytz
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.transaction import commit
from sqlparse.utils import remove_quotes

from SHOP import settings
from .authenticate import PhoneBackend
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from random import randint

from accounts.forms import UserRegisterForm, OtpForm, EditProfileForm, SetPasswordForm, AddressForm
from accounts.models import Otp, User, Address


class UserRegisterView(View):
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('home:home')
    #     else:
    #         return super().dispatch(request, *args, **kwargs)
    form_class = UserRegisterForm
    def get(self,request):
        form = self.form_class()
        return render(request, 'accounts/login.html',{'form':form})

    def post(self,request):
        form =self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            phone_number = request.session['phone_number'] = cd.get('phone_number')
            code = randint(1000, 9999)
            print(f'otp code is :{code}')
            Otp.objects.create(username=phone_number, code=code)
            return redirect('accounts:otp')
        return render(request, 'accounts/login.html',{'form':form})


class OtpRegisterView(View):
    form = OtpForm
    def get(self,request):
        form = self.form()
        return render(request, 'accounts/otp.html', {'form':form})
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            code = cd['code1']+cd['code2']+cd['code3']+cd['code4']
            otp_code=Otp.objects.get(username=request.session['phone_number'])
            if code != otp_code.code:
                messages.error(request,'کداشتباه است', 'danger')
                return redirect('accounts:otp')
            if otp_code.created < datetime.now(tz=pytz.timezone('Asia/Tehran'))-timedelta(minutes=2):
                messages.error(request, 'کد منقضی شده', 'danger')
                return redirect('accounts:otp')
            user, is_user = User.objects.get_or_create(phone_number=request.session['phone_number'])
            login(request, user, backend='accounts.authenticate.PhoneBackend')
            otp_code.delete()
            messages.success(request, 'ثبت نام شما با موفقیت انجام شد', 'success')
            return redirect('accounts:edit_profile')



class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return redirect('home:home')

class EditProfileView(LoginRequiredMixin, View):
    form_instance = EditProfileForm
    is_active = 'inactive'
    def setup(self, request, *args, **kwargs):
        self.is_active = 'active'
        return super().setup(request, *args, **kwargs)
    def get(self, request):
        form = self.form_instance(initial={'fullname':request.user.fullname, 'email':request.user.email})
        return render(request, 'accounts/edit-profile.html', {'form':form, 'is_active_profile':self.is_active})

    def post(self, request):
        form = self.form_instance(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = request.user
            user.fullname = cd.get('fullname')
            user.email = cd.get('email')
            user.save()
            messages.success(request, 'تغییرات با موفقیت ذخیره شد', 'success')
            return render(request, 'accounts/edit-profile.html', {'form':form, 'is_active_profile':self.is_active})
        messages.error(request, 'فرم معتبرنیست', 'danger')
        return redirect('accounts:edit_profile')

class SetOrChangePasswordView(LoginRequiredMixin, View):
    form_class = SetPasswordForm
    is_active = 'inactive'

    def setup(self, request, *args, **kwargs):
        self.is_active = 'active'
        return super().setup(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/change-password.html',
                      {'form':form, 'is_active_password':self.is_active})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = request.user
            user.set_password(cd.get('password1'))
            user=user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request,'پسورد با موفقیت ذخیره شد', 'success')
            return redirect('accounts:edit_profile')
        return render(request, 'accounts/change-password.html',
                      {'form': form, 'is_active_password': self.is_active})

class AddressView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        if Address.objects.filter(user=request.user):
            return super().dispatch(*args, **kwargs)
        return redirect('accounts:add_address')
    def get(self, request):
        return render(request, 'accounts/delivery-address.html')

class AddressAddView(View):
    def get(self, request):
        return render(request, 'accounts/address-create.html')
    form_class = AddressForm
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return render(request, 'accounts/address-create.html')