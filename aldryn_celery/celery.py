# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf import settings

import aldryn_django.startup
from celery import Celery


aldryn_django.startup._setup(settings.BASE_DIR)

app = Celery('aldryn_celery')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
