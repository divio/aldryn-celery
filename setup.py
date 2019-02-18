# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


# from https://gist.github.com/techtonik/4066623
def get_version(relpath):
    """Read version info from a file without importing it."""
    from os.path import dirname, join

    if '__file__' not in globals():
        # Allow to use function interactively
        root = '.'
    else:
        root = dirname(__file__)

    # The code below reads text file with unknown encoding in
    # in Python2/3 compatible way. Reading this text file
    # without specifying encoding will fail in Python 3 on some
    # systems (see http://goo.gl/5XmOH). Specifying encoding as
    # open() parameter is incompatible with Python 2

    # cp437 is the encoding without missing points, safe against:
    #   UnicodeDecodeError: 'charmap' codec can't decode byte...

    for line in open(join(root, relpath), 'rb'):
        line = line.decode('cp437')
        if '__version__' in line:
            if '"' in line:
                # __version__ = "0.9"
                return line.split('"')[1]
            elif "'" in line:
                return line.split("'")[1]


REQUIREMENTS = [
    'aldryn-django',
    'django-celery',
    'celery==3.1.25',
]


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Framework :: Django',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.0',
    'Framework :: Django :: 2.1',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]


setup(
    name='aldryn-celery',
    version=get_version('aldryn_celery/__init__.py'),
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/divio/aldryn-celery',
    license='BSD',
    description='An opinionated Celery setup bundled as an Aldryn Addon. To be used together with aldryn-django.',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    test_suite='tests.settings.run',
    entry_points = {
        'console_scripts': ['aldryn-celery=aldryn_celery.cli:main'],
    },
)
