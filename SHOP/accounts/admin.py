from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.forms import UserChangeForm, UserCreationForm
from accounts.models import User, Otp


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ['fullname', 'phone_number', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = [
        (None, {'fields':['email', 'phone_number', 'fullname', 'password']}),
        ('permissions', {'fields':['is_admin', 'is_active']})
    ]

    add_fieldsets = [
        (None, {'fields':['email', 'phone_number', 'fullname','password1', 'password2']}),
        ('permissins', {'fields': ['is_active', 'is_admin']})
    ]
    search_fields = ['phone_number']
    ordering = ['fullname']
    filter_horizontal = []

class OtpAdmin(admin.ModelAdmin):
    list_display = ['username', 'code', 'created']
    fields = ['username', 'code']


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Otp, OtpAdmin)
