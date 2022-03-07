#!/usr/bin/env python

from distutils.core import setup

setup(
    name="rssagg",
    version="0.1.0",
    description="RSS Aggregator",
    long_description=open("README.md").read(),
    author="Roi Gabay",
    author_email="roigby@gmail.com",
    url="https://www.python.org/gabay/rssagg/",
    packages=["rssagg"],
    install_requires=["requests", "bs4", "lxml"],
)
