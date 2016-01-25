# -*- coding: utf-8 -*-
from functools import partial
from aldryn_client import forms


class Form(forms.BaseForm):

    def to_settings(self, data, settings):
        from aldryn_addons.utils import djsenv
        s = settings
        env = partial(djsenv, settings=settings)

        s['BROKER_URL'] = env('BROKER_URL')
        s['ENABLE_CELERY'] = env('ENABLE_CELERY', bool(s['BROKER_URL']))
        if not s['ENABLE_CELERY']:
            return settings
        s['INSTALLED_APPS'].append('aldryn_celery')
        s['INSTALLED_APPS'].append('djcelery')
        s['CELERYBEAT_SCHEDULER'] = env('CELERYBEAT_SCHEDULER', 'djcelery.schedulers.DatabaseScheduler')

        s['CELERY_RESULT_BACKEND'] = env('CELERY_RESULT_BACKEND', 'djcelery.backends.database.DatabaseBackend')
        s['CELERY_TASK_RESULT_EXPIRES'] = env('CELERY_TASK_RESULT_EXPIRES', 5*60*60)
        s['CELERY_ACCEPT_CONTENT'] = env('CELERY_ACCEPT_CONTENT', ['json'])
        s['CELERY_TASK_SERIALIZER'] = env('CELERY_TASK_SERIALIZER', 'json')

        s['CELERYD_PREFETCH_MULTIPLIER'] = env('CELERYD_PREFETCH_MULTIPLIER', 1)
        s['CELERY_ACKS_LATE'] = env('CELERY_ACKS_LATE', True)

        s['CELERYBEAT_SCHEDULE'] = env('CELERYBEAT_SCHEDULE', {
            # 'my-task-name': {
            #     'task': '',
            #     'schedule': '',
            #     'kwargs': {},
            #     'options': {},
            # },
        })
        return s
