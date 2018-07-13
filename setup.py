#!/usr/bin/env python
from setuptools import setup
name = "code_engine"

requires = ['demjson'],

setup(
    name = name,
    version = '1.0.0',
    author = 'Zongying Cao',
    author_email = 'zongying.cao@dxc.com',
    description = 'code engine',
    long_description = 'code engine',
    url = 'https://github.com/cao5zy/code-engine',
    packages = [name],
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
