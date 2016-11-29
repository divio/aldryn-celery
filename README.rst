#############
Aldryn Celery
#############

|PyPI Version|

An opinionated Celery setup bundled as an Aldryn Addon.
To be used together with aldryn-django.

======================
Installation & Updates
======================

*********************
Aldryn Platform Users
*********************

Ask Aldryn staff to add this Addon to your Project. It is currently still
hidden.

Aldryn staff has to:
 * provision a rabbitmq vhost and set the ``BROKER_URL`` environment variable.
 * configure the additional worker processes to run in the background (celeryd,
   celerybeat and celerycam)


*******************
Manual Installation
*******************

tbd.


=====
Usage
=====

rough notes:

see ``aldryn_config.py`` to see the environment variables that can be used as
knobs.

Use the following commands to start the celery processes:

* ``aldryn-celery worker``
* ``aldryn-celery beat``
* ``aldryn-celery cam``

==============================
Local setup on Aldryn Platform
==============================

Add the following services to your ``docker-compose.yml`` file::
   
    celeryworker:
      command: aldryn-celery worker
    celerybeat:
      command: aldryn-celery beat
    celerycam:
      command: aldryn-celery cam
    rabbitmq:
      image: rabbitmq:3.5-management
      hostname: rabbitmq
      ports:
        - "15672:15672"
      expose:
        - "15672"
      environment:
        RABBITMQ_ERLANG_COOKIE: "secret cookie here"
   
For ``celeryworker``, ``celerybeat`` and ``celerycam`` copy in all the options from the ``web`` service, except ``ports``.

In ``web``, ``celeryworker``, ``celerybeat`` and ``celerycam`` add::

    links:
      - "rabbitmq:rabbitmq"

In ``.env-local`` add the following::

    RABBITMQ_ERLANG_COOKIE="secret cookie here"
    BROKER_URL="amqp://guest:guest@rabbitmq:5672/"

``docker-compose up`` or ``divio project up`` will now also startup celery.
Run ``docker-compose stop web && docker-compose rm web && docker-compose up -d web`` for the ``web`` service to pick up the new env vars.
Keep in mind, that celery does not auto reload on code changes. So you need to ``docker-compose restart celeryworker`` after every code change.

.. |PyPI Version| image:: http://img.shields.io/pypi/v/aldryn-celery.svg
   :target: https://pypi.python.org/pypi/aldryn-celery
