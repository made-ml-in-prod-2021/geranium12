#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pkutils
from pkg_resources import parse_requirements
from setuptools import find_packages, setup

requirements = list(pkutils.parse_requirements('requirements.txt'))

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    install_requires=requirements,
    description='Production-ready project for heart disease classification',
    author='Hanna Herasimchyk',
    license='MIT',
)
