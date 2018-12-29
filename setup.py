from os import path
from codecs import open

import subprocess

import sys

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
        'git_additions',
        'git_additions.reports',
        'git_additions.reports.duration',
        'git_additions.reports.exporter',
        'git_additions.reports.logs',
        'git_additions.reports.stats',
        'git_additions.reports.users',
    ]


def version():
    __version = '0.0.4'
    if path.exists('.git'):
        __build = subprocess.check_output('git rev-list HEAD --count'.split()).decode().strip()
    else:
        __build = 'b'
    return '%s.%s' % (__version, __build)


setup(
    version=version(),
    long_description=long_description(),
    install_requires=[
        'pygit2', 'colorama'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'git-duration=git_additions.reports.duration:runner',
            'git-logs=git_additions.reports.logs:runner',
            'git-stats=git_additions.reports.stats:runner',
            'git-users=git_additions.reports.users:runner',
        ],
    },
)
