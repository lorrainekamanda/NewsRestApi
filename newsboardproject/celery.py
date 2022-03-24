from __future__ import absolute_import

import os
import django
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsboardproject.settings')
django.setup()

app.conf.beat_schedule = {
    'restart-votes-count': {
        'task': 'newsboardapi.tasks.restart_votes',
        'schedule': crontab(hour=0, minute=0)  # everyday at midnight
    }


if __name__ == '__main__':
    app.start()