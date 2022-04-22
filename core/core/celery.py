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

app.config_from_object('django.conf:settings')
app.conf.beat_schedule = {
    'get-rate-every-day-at-12am':{
        'task': 'airflow.tasks.currency_rate',
        # 'schedule': crontab(hour=00, minute=00),
        'schedule': 15,
    }
}
app.autodiscover_tasks(settings.INSTALLED_APPS)
