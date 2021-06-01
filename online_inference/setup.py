#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name="online_inference",
    packages=find_packages(),
    version="0.1.0",
    install_requires=[
        "omegaconf~=2.0.6",
        "pandas~=1.1.3",
        "pydantic~=1.8.2",
        "requests~=2.25.1",
        "numpy~=1.20.2",
        "setuptools~=56.0.0",
        "pytest~=6.2.3",
        "fastapi~=0.65.1",
        "uvicorn~=0.13.4",
    ],
    description="Online inference for homework1",
    author="Hanna Herasimchyk",
    license="MIT",
)
