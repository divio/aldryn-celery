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
        s['INSTALLED_APPS'].append('djcelery')
        # aldryn_celery must be after djcelery so it can manipulate its admin
        s['INSTALLED_APPS'].append('aldryn_celery')
        s['CELERYBEAT_SCHEDULER'] = env('CELERYBEAT_SCHEDULER', 'djcelery.schedulers.DatabaseScheduler')
        s['CELERY_RESULT_BACKEND'] = env('CELERY_RESULT_BACKEND', 'djcelery.backends.database:DatabaseBackend')

        s['CELERY_TASK_RESULT_EXPIRES'] = env('CELERY_TASK_RESULT_EXPIRES', 5*60*60)
        s['CELERY_ACCEPT_CONTENT'] = env('CELERY_ACCEPT_CONTENT', ['json'])
        s['CELERY_TASK_SERIALIZER'] = env('CELERY_TASK_SERIALIZER', 'json')


        s['CELERYD_PREFETCH_MULTIPLIER'] = env('CELERYD_PREFETCH_MULTIPLIER', 1)
        s['CELERY_ACKS_LATE'] = env('CELERY_ACKS_LATE', True)

        s['CELERY_TRACK_STARTED'] = env('CELERY_TRACK_STARTED', True)

        # rate limits add a huge amount of complexity to celery code and thus
        # potential for things to go wrong. They are also very rarely used.
        # Disable them by default.
        s['CELERY_DISABLE_RATE_LIMITS'] = env('CELERY_DISABLE_RATE_LIMITS', True)

        # Tell the celery worker master process to use the 'fair' optimisation
        # profile. This prevents cases where workers get tasks assigned, even
        # though they are still handling long running tasks.
        # CELERY_OPTIMIZATION_PROFILE is not an official celery setting. We
        # just use it in our cli to add the -Ofair option.
        s['CELERY_OPTIMIZATION_PROFILE'] = env('CELERY_OPTIMIZATION_PROFILE', 'fair')

        s['CELERYBEAT_SCHEDULE'] = env('CELERYBEAT_SCHEDULE', {
            # 'my-task-name': {
            #     'task': '',
            #     'schedule': '',
            #     'kwargs': {},
            #     'options': {},
            # },
        })
        s['CELERY_REDIRECT_STDOUTS_LEVEL'] = env('CELERY_REDIRECT_STDOUTS_LEVEL', 'INFO')
        s['CELERYD_CONCURRENCY'] = env('CELERYD_CONCURRENCY', '2')
        s['CELERY_SEND_EVENTS'] = env('CELERY_SEND_EVENTS', True)

        s['CELERY_CAM_CLASS'] = env('CELERY_CAM_CLASS', 'djcelery.snapshot.Camera')
        s['CELERY_CAM_FREQUENCY'] = env('CELERY_CAM_FREQUENCY', 10)

        # celery uses CELERY_ENABLE_UTC=True as default and djcelery (and thus
        # celerycam) uses CELERY_ENABLE_UTC=False as default. This causes
        # timestamp offsets when checking for worker heartbeats (and possibly
        # other problems). So we need to set it explicitly here.
        s['CELERY_TIMEZONE'] = 'UTC'
        s['CELERY_ENABLE_UTC'] = True

        s['LOGGING']['loggers']['celery'] = {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
        return s
