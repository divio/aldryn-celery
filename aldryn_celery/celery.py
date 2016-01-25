# -*- coding: utf-8 -*-
from __future__ import absolute_import
import aldryn_django.startup
import os
import sys
from celery import Celery

# this code is very similar to aldryn_django.startup

# add the current directory to pythonpath. So the project files can be read.
BASE_DIR = os.getcwd()
sys.path.insert(0, BASE_DIR)
if not os.path.exists(os.path.join(BASE_DIR, 'manage.py')):
    raise RuntimeError('make sure you are in the same directory as manage.py')
aldryn_django.startup._setup(BASE_DIR)


from django.conf import settings  # noqa

app = Celery('aldryn_celery')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
