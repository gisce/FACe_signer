# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from FACe_signer import __version__

with open('requirements.txt', 'r') as f:
    INSTALL_REQUIRES = f.readlines()

setup(
    name='FACe_signer',
    description='Zeep plugin that signs FACe SOAP requests',
    version=__version__,
    url='http://www.gisce.net',
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    license='GNU GPLv3',
    provides=['FACe_signer'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
