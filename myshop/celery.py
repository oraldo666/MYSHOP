from __future__ import unicode_literals, absolute_import
import os

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'myshop.settings')

app = Celery('myshop', include=["shopitems.tasks"])
app.conf.enable_utc = False
app.conf.update(timezone='Europe/Berlin')

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
