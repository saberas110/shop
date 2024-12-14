import pytz
from celery import shared_task
from .models import Otp
from datetime import timedelta, datetime

@shared_task
def delete_auto_otp():
    expired_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
    Otp.objects.filter(created__lt=expired_time).delete()
    print('start')
