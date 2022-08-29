# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in intech_fire/__init__.py
from intech_fire import __version__ as version

setup(
	name='intech_fire',
	version=version,
	description='Intech Fire',
	author='New Indictrans Technologies Pvt.Ltd',
	author_email='contact@indictranstech.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
