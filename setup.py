#!/usr/bin/env python
from setuptools import setup

requires = ['demjson'],

setup(
    name = 'code_engine',
    version = '1.2.1',
    author = 'Zongying Cao',
    author_email = 'zongying.cao@dxc.com',
    description = 'code engine',
    long_description = 'code engine',
    url = 'https://github.com/cao5zy/code-engine',
    packages = ['code_engine'],
    install_requires = requires,
    license = 'Apache',
    classifiers = [
               'Development Status :: 4 - Beta',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: Apache Software License',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development :: Libraries',
           ],
)
