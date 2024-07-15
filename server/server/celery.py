from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

# Create a Celery application instance
app = Celery('server')

# Load configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Define periodic tasks (Celery Beat)
app.conf.beat_schedule = {
    'run-arbitrage-task-every-minute': {
        'task': 'django.core.management.call_command',  # Run Django management command
        'args': ('calculate_arbitrage',),  # Arguments for the management command
        'schedule': crontab(minute='*/1'),  # Run every minute
    },
}

# Automatically discover task modules in applications listed in INSTALLED_APPS
app.autodiscover_tasks()
