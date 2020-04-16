from celery import Celery
import os
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CHEN.settings")

app = Celery("huyue")

app.conf.update(
    BORKER_URL = "redis://127.0.0.1:6379/0"
)

app.autodiscover_tasks(settings.INSTALLED_APPS)
