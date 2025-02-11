import re
from setuptools import setup, find_packages
# FileNotFoundError is not there in Python 2, define it:
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

with open('gixy/__init__.py', 'r') as fd:
    version = re.search(r'^version\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

# README.md is not present in Docker image setup
long_description = None
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    pass

setup(
    name='gixy-ng',
    version=version,
    description='NGINX configuration [sec]analyzer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='nginx security lint static-analysis',
    author='Yandex IS Team, GetPageSpeed LLC',
    author_email='buglloc@yandex.ru, info@getpagespeed.com',
    url='https://github.com/dvershinin/gixy',
    install_requires=[
        'pyparsing>=1.5.5,<=2.4.7',
        'cached-property>=1.2.0;python_version<"3.8"',
        'argparse>=1.4.0;python_version<"3.2"',
        'six>=1.1.0',
        'Jinja2>=2.8',
        'ConfigArgParse>=0.11.0'
    ],
    entry_points={
        'console_scripts': ['gixy=gixy.cli.main:main'],
    },
    test_suite='nose.collector',
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing'
    ],
    include_package_data=True
)
