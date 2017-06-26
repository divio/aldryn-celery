# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import sys
import aldryn_django.startup

from celery import Celery

from django.conf import settings


BASE_DIR = os.getcwd()

if BASE_DIR not in sys.path:
    # Adds the current directory to python path.
    # This is required for django to find the settings module
    sys.path.insert(0, BASE_DIR)

# Sets DJANGO_SETTINGS_MODULE environment variable
aldryn_django.startup._setup(path=None)

app = Celery('aldryn_celery')
app.config_from_object(settings)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
