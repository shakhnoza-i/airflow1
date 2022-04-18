from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Almaty')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
# app.config_from_object('django.conf:settings')
app.config_from_object('django.conf:settings')
app.conf.beat_schedule = {
    'get-rate-every-day-at-12am':{
        'task': 'airflow.tasks.CurrencyRate',
        'schedule': 30,
        # 'schedule': crontab(hour=12, minute=00),
        # 'args':
    }
}
app.autodiscover_tasks(settings.INSTALLED_APPS)

