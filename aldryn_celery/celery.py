# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import sys
import aldryn_django.startup

from celery import Celery

from django.conf import settings

# Adds the current directory to python path.
# This is required for django to find the settings module
sys.path.insert(0, os.getcwd())

# Sets DJANGO_SETTINGS_MODULE environment variable
# Calls django.setup() to setup app registry
aldryn_django.startup.setup(path=None)

app = Celery('aldryn_celery')
app.config_from_object(settings)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
