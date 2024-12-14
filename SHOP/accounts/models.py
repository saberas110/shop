import pytz
from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=100)
    fullname = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'phone_number'

    objects = UserManager()

    def __str__(self):
        return f'{self.fullname} - {self.phone_number}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Otp(models.Model):
    username = models.CharField(max_length=11)
    code = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f'{self.username}-{self.code},  {self.created}'
