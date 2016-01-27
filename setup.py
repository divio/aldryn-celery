# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


# from https://gist.github.com/techtonik/4066623
def get_version(relpath):
    """Read version info from a file without importing it"""
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



setup(
    name="aldryn-celery",
    version=get_version('aldryn_celery/__init__.py'),
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
    entry_points='''
        [console_scripts]
        aldryn-celery=aldryn_celery.cli:main
    ''',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Framework :: Django',
    ]
)
