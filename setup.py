# -*- coding: utf-8 -*-

import os
from setuptools import setup

__version__ = '0.8.1'

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-select2-rocks',
    version=__version__,
    packages=['select2rocks'],
    include_package_data=True,
    license='BSD License',
    description='A Django application to provide AJAX autocomplete with Select2.',
    long_description=README,
    author='Stéphane Raimbault',
    author_email='stephane.raimbault@polyconseil.fr',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
