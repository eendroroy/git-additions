from os import path
from codecs import open

import subprocess

import sys

import time
from setuptools import setup

if sys.version_info[:2] < (3, 0):
    raise RuntimeError("Python version 3 required.")


def long_description():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_desc = f.read()
    return long_desc


def find_packages(*args, **kwargs):
    return [
        'git_reports',
        'git_reports.reports',
        'git_reports.reports.exporter',
        'git_reports.reports.log',
        'git_reports.reports.stats'
    ]


def install_requires():
    return [
        'pygit2'
    ]


def version():
    __version = '0.0.3'
    if path.exists('.git'):
        __build = subprocess.check_output('git rev-list HEAD --count'.split()).decode().strip()
    else:
        __build = 'b'
    return '%s.%s.%s' % (__version, __build, int(time.mktime(time.gmtime())))


setup(
    version=version(),
    long_description=long_description(),
    install_requires=install_requires(),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'git-report=git_reports:main',
        ],
    },
)
