from os import path
from codecs import open
from setuptools import setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def find_packages(*args, **kwargs):
    return ['git-reports']

setup(
    name='git-reports',
    version='0.1.2',
    description='A command line tool to generate various git reports.',
    long_description=long_description,
    url='https://github.com/eendroroy/git-reports',
    author='indrajit',
    author_email='eendroroy@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'report=git-reports:main',
        ],
    },
)
