# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.contrib import admin
from django.utils import timezone
from django.utils.timesince import timesince

import djcelery.admin
import djcelery.models


# show heartbeat on WorkerState
class WorkerMonitor(djcelery.admin.WorkerMonitor):
    list_display = djcelery.admin.WorkerMonitor.list_display + (
        'last_heartbeat',
        'since_last_heartbeat',
    )

    def since_last_heartbeat(self, obj):
        if obj.last_heartbeat:
            timesince_exact = timezone.now() - obj.last_heartbeat
            timesince_pretty = timesince(obj.last_heartbeat)
            return u'<div title="{}">{}</div>'.format(timesince_exact, timesince_pretty)

        return None
    since_last_heartbeat.allow_tags = True


admin.site.unregister(djcelery.models.WorkerState)
admin.site.register(djcelery.models.WorkerState, WorkerMonitor)
