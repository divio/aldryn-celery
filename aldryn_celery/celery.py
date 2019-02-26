# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf import settings  # noqa

import aldryn_django.startup
from celery import Celery


# `path` is not used anymore but still required
aldryn_django.startup._setup(path=None)


app = Celery('aldryn_celery')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
