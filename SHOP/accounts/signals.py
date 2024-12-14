import asyncio
from datetime import datetime
from time import sleep

from .models import Otp
from .views import OtpRegisterView
from django.dispatch import receiver
from django.db.models.signals import post_save,post_init
from django.core.signals import request_finished
from django.core.handlers.wsgi import WSGIHandler
#
# @receiver(request_finished, sender=)
# def del_otp(sender, **kwargs):
#     print('start')
#     print('done')