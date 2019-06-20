#!/usr/bin/env python3

import os
from setuptools import setup

# get key package details from bitrue/__version__.py
about = {}  # type: ignore
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'bitrue', '__version__.py')) as f:
    exec(f.read(), about)



# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(
    name=about['__title__'],
    description=about['__description__'],
    long_description_content_type='text/markdown',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=['bitrue'],
    include_package_data=True,
    python_requires=">=3.7.*",
    install_requires=['numpy', 'requests'],
    license=about['__license__'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='package development template'
)
