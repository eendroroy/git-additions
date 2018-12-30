import subprocess
from codecs import open
from os import path

import setuptools
from setuptools import setup


def long_description():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_desc = f.read()
    return long_desc


def version():
    __version = '0.1.0'
    if path.exists('.git'):
        __build = subprocess.check_output('git rev-list HEAD --count'.split()).decode().strip()
    else:
        __build = 'b'
    return '%s.%s' % (__version, __build)


setup(
    version=version(),
    long_description=long_description(),
    install_requires=[
        'pygit2', 'colorama', 'pathlib'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
    ],
    entry_points={
        'console_scripts': [
            'git-duration=git_additions.additions.duration:runner',
            'git-logs=git_additions.additions.logs:runner',
            'git-stats=git_additions.additions.stats:runner',
            'git-users=git_additions.additions.users:runner',
        ],
    },
)
