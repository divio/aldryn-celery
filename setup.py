# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_celery import __version__

setup(
    name="aldryn-celery",
    version=__version__,
    description='An opinionated Celery setup bundled as an Aldryn Addon. To be used together with aldryn-django.',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-celery',
    packages=find_packages(),
    install_requires=(
        'aldryn-django',
        'django-celery',
        'celery',
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Framework :: Django',
    ]
)
