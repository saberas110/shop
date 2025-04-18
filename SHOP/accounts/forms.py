from cProfile import label

from django.contrib.admin.utils import label_for_field
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User, Otp, Address
from django import forms


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password confirmation', widget=forms.PasswordInput)

    class meta:
        model = User
        fields = ['email', 'phone_number', 'fullname']

    def clean_password2(self):
        cd = self.cleaned_data
        password1 = cd.get('password1')
        password2 = cd.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValueError('passwors don\'t match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'fullname', 'password', 'is_active', "is_admin"]


class UserRegisterForm(forms.Form):
    phone_number = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'style': 'width:200%'

    }))

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        print(phone_number)
        if len(phone_number) != 11:
            raise ValidationError('شماره وارد شده صحیح نمی باشد.')
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('کاربری با این شماره از قبل وجود دارد')

        Otp.objects.filter(username=phone_number).delete()
        return phone_number


class OtpForm(forms.Form):
    code1 = forms.CharField(max_length=1, label='', widget=forms.TextInput(attrs={
        'placeholder': "_",
        'type': "number",
        'step': "1",
        'min': "0",
        'max': "9",
        'autocomplete': "no",
        'pattern': "\d*",
        'max_length ': '1'
    }))
    code2 = forms.CharField(max_length=1, label='', widget=forms.TextInput(attrs={
        'placeholder': "_",
        'type': "number",
        'step': "1",
        'min': "0",
        'max': "9",
        'autocomplete': "no",
        'pattern': "\d*",
        'max_length ': '1'
    }))
    code3 = forms.CharField(max_length=1, label='', widget=forms.TextInput(attrs={
        'placeholder': "_",
        'type': "number",
        'step': "1",
        'min': "0",
        'max': "9",
        'autocomplete': "no",
        'pattern': "\d*",
        'max_length ': '1'
    }))
    code4 = forms.CharField(max_length=1, label='', widget=forms.TextInput(attrs={
        'placeholder': "_",
        'type': "number",
        'step': "1",
        'min': "0",
        'max': "9",
        'autocomplete': "no",
        'pattern': "\d*",
        'max_length ': '1'
    }))


class EditProfileForm(forms.Form):
    fullname = forms.CharField(label='', widget=forms.TextInput(attrs={
        'type': "text",
        'class': "form-control",
        'id': "floatingInputName",
        "placeholder": "نام و نام خانوادگی خود را وارد کنید...",
    }))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'type': "text",
        'class': "form-control",
        'id': "floatingInputName",
        "placeholder": "ایمیل خود را وارد کنید...",
    }))


class SetPasswordForm(forms.Form):
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'id': "floatingInputNewPasswd",
        'placeholder': "رمز عبور جدید خود را وارد کنید ...",
    }))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'id': "floatingInputNewPasswd",
        'placeholder': "رمز عبور جدید خود را دوباره وارد کنید ...",
    }))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise ValidationError('پسورد ها مشابه نیستند')
        if len(cd['password2'])<8:
            raise ValidationError('پسورد حداقل باید ۸ کاراکتر باشد')
        return cd['password2']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('__all__')
        widgets = {
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingInputStreet1',
                'style': 'max-width:95%;height:200px',
                'placeholder': 'ادرس خود را وارد کنید'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width:40%',
                'placeholder': 'شماره تماس خود را وارد کنید'

            }),
            'province': forms.TextInput(attrs={
                'class': 'form-control',
                'id': "floatingInputOstan1",
                'style': 'max-width:40%',
                'placeholder': 'نام استان  خود را وارد کنید'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingInputCity1',
                'style': 'max-width:40%',
                'placeholder': 'نام شهر خود را وارد کنید'
            }),


        }
