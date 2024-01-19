#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

config = {
    'name': 'emuobject',
    'author': 'Ovid',
    'author_email': 'curtis.poe@gmail.com',
    'url': 'https://github.com/Ovid/emuobject',
    'description': 'Type-safe, immutable objects',
    'long_description': open('README.rst', 'r').read(),
    'license': 'MIT',
    'version': '0.0.1',
    'install_requires': [
		'cerberus',
        'termcolor',
	],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning",
    ],
    'packages': find_packages(),
}

if __name__ == '__main__':
    setup(**config)
