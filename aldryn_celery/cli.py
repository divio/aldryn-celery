#-*- coding: utf-8 -*-
from __future__ import absolute_import
import click
import os
import sys
from django.conf import settings as django_settings


# add the current directory to pythonpath. So the project files can be read.
BASE_DIR = os.getcwd()
sys.path.insert(0, BASE_DIR)


@click.command()
@click.pass_obj
def worker(ctx_obj):
    """
    launch a celery worker
    """
    execute(start_worker_command(settings=ctx_obj['settings']))


@click.command()
@click.pass_obj
def cam(ctx_obj):
    """
    launch celerycam
    """
    execute(start_cam_command(settings=ctx_obj['settings']))


@click.command()
@click.pass_obj
def beat(ctx_obj):
    """
    launch celerybeat
    """
    execute(start_beat_command(settings=ctx_obj['settings']))


@click.command(name='all')
@click.pass_obj
def start_all(ctx_obj):
    """
    coming soon: launch the background worker
    """
    # TODO: celery worker startup, once available
    pass


@click.group()
@click.option('--verbose', is_flag=True)
@click.pass_context
def main(ctx, verbose):
    if not os.path.exists(os.path.join(BASE_DIR, 'manage.py')):
        raise click.UsageError('make sure you are in the same directory as manage.py')

    from aldryn_django import startup
    startup._setup(BASE_DIR)

    ctx.obj = {
        'settings': {key: getattr(django_settings, key) for key in dir(django_settings)}
    }


main.add_command(worker)
main.add_command(cam)
main.add_command(beat)
main.add_command(start_all)


def execute(args, script=None):
    # TODO: is cleanup needed before calling exec? (open files, ...)
    command = script or args[0]
    os.execvp(command, args)


def start_worker_command(settings):
    cmd = [
        'celery',
        '--app=aldryn_celery',
        'worker',
    ]
    if settings['CELERYD_OPTIMIZATION_PROFILE']:
        cmd.append('-O{}'.format(settings['CELERYD_OPTIMIZATION_PROFILE']))
    return cmd


def start_cam_command(settings):
    return [
        'celery',
        '--app=aldryn_celery',
        'events',
        '--camera={}'.format(settings['CELERY_CAM_CLASS']),
        '--frequency={}'.format(settings['CELERY_CAM_FREQUENCY']),
        '--pidfile=',
    ]


def start_beat_command(settings):
    return [
        'celery',
        '--app=aldryn_celery',
        'beat',
        '--pidfile=',
    ]
