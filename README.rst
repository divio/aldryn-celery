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



.. |PyPI Version| image:: http://img.shields.io/pypi/v/aldryn-celery.svg
   :target: https://pypi.python.org/pypi/aldryn-celery
