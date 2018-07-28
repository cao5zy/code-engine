#!/usr/bin/env python
from setuptools import setup, find_packages
name = "code_engine"

requires = ['demjson==2.2.4', 'Jinja2==2.10', 'codegenhelper>=0.0.9', 'request>=2.19.1'],

setup(
    name = name,
    version = '1.0.11',
    author = 'Zongying Cao',
    author_email = 'zongying.cao@dxc.com',
    description = 'Code-engine is a dead simple engine based on Jinja2 to make you free from generation process.',
    long_description = """Code-engine is a dead simple engine based on Jinja2 to make you free from generation process.
    It looks like a pipe. You push your data into the end of the pipe. Finally, the files will be generated at the other end.""",
    url = 'https://github.com/cao5zy/code-engine',
    packages = [name, "code_engine.util"],
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
