#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

readme = open('README.md').read()

# get the requirements from the requirements.txt
requirements_file = open('requirements.txt').read().split()
requirements = requirements_file

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='racktables',
    version='0.0.7',
    description='Racktables API python wrapper',
    long_description=readme,
    author='Wagner Sartori Junior',
    author_email='wsartori@comscore.com',
    url='https://github.com/trunet/racktables-py-client',
    packages=[
        'racktables',
    ],
    package_dir={'racktables':
                 'racktables'},
    include_package_data=True,
    install_requires=requirements,
    license="In-house",
    zip_safe=False,
    keywords='racktables',
    entry_points={
        'console_scripts': [
            # enable this to automatically generate a script in /usr/local/bin called myscript that points to your
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
)

