#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='python-bitrue',
    version='0.0.1',
    packages=['bitrue'],
    description='Bitrue REST API python implementation',
    url='https://github.com/snub-fighter/python-bitrue',
    author='snub-fighter',
    license='MIT',
    author_email='',
    install_requires=['sys','logging','configparser','tabulate','multiprocessing','selenium','hashlib','hmac','time','operator','atexit','apscheduler','requests', 'six', 'Twisted', 'pyOpenSSL', 'autobahn', 'service-identity', 'dateparser', 'urllib3', 'chardet', 'certifi', 'cryptography', ],
    keywords='bitrue exchange rest api xrp bitcoin ethereum btc eth neo',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
