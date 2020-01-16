# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in meraki/__init__.py
from meraki import __version__ as version

setup(
	name='meraki',
	version=version,
	description='Send Custom Cake Orders to Telegram Messenger',
	author='Proenterprise Ventures',
	author_email='support@erp.co.zm',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
