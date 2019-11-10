# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in tenant_management/__init__.py
from tenant_management import __version__ as version

setup(
	name='tenant_management',
	version=version,
	description='app for tenant',
	author='chibuzo',
	author_email='chiboy.madu90@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
