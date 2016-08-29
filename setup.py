#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import writer

setup(
    name='writer.py',
    version=writer.__version__,


    packages=find_packages(),

    author="Rousseau Alexandre",
    author_email="rousseaualexandre.lyon@gmail.com",

    description="a simply class used to normalize all inputs/outputs in console",

    long_description=open('README.md').read(),

    url='https://github.com/madeindjs/writer',


    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries ",
        "Topic :: Software Development :: Libraries :: Python Modules ",

    ],


)
