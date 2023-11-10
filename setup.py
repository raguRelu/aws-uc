import codecs
import os
import re

from setuptools import setup


dirname = os.path.abspath(os.path.dirname(__file__))

with codecs.open(
    os.path.join(dirname, "undetected_chromedriver", "__init__.py"),
    mode="r",
    encoding="utf-8",
) as fp:
    try:
        version = re.findall(r"^__version__ = ['\"]([^'\"]*)['\"]", fp.read(), re.M)[0]
    except Exception:
        raise RuntimeError("unable to determine version")


setup(
    name="undetected-chromedriver",
    version=version,
    packages=["undetected_chromedriver"],
    install_requires=[
        "selenium==4.9.1",
        "requests",
        "websockets",
    ],

    license="GPL-3.0",
    author="UltrafunkAmsterdam",
    author_email="info@blackhat-security.nl",

    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
