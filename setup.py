#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup,find_packages

setup(
    name = 'autocompletekeywords',
    version = 1.0,
    author = 'Grzegorz Sobanski',
    author_email = 'silk@boktor.net',
    description = 'Dynamic list of suggestions in keywrods field.',
    long_description = '''
Provides a dynamic suggest box for the keywords when editing tickets.
''',
    license = 'BSD',
    packages = find_packages(),
    package_data = {
        'autocompletekeywords': ['*.txt', 'htdocs/css/*.css', 'htdocs/js/*.js']
    },

    entry_points = {
        'trac.plugins': [
            'autocompletekeywords = autocompletekeywords',
        ],
    },
)
