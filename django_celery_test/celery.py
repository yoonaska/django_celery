from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab




os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery_test.settings")

app = Celery("django_celery_test")
app.conf.enable_utc = False


app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace="CELERY")



app.conf.beat_schedule = {
    'run_every_minute':{
        'task': 'apps.feedback.tasks.send_mail_task',
        # 'schedule' : crontab(hour=12, minute=44),
        'schedule': crontab(minute='*')
        # 'args':
    }
}

app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print(f'Request : {self.request!r}')
