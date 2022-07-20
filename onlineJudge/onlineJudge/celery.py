from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from .settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CornerCase.settings')
app = Celery('CornerCase',broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
app.config_from_object('django.conf:settings', namespace='CELERY')
# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()
