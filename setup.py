#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import io
from os import path
from setuptools import setup, find_packages

# --- Résolution du chemin pour le README ---
here = path.abspath(path.dirname(__file__))


try:
    with io.open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Un outil Python pour télécharger les données boursières de la BRVM."

setup(
    name='brvmfinance',
    version='0.1.1',
    description='Download market data from BRVM (Bourse Régionale des Valeurs Mobilières)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SORADATA/brvmfinance',
    author='soradata',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    platforms=['any'],
    keywords='pandas, brvm, finance, afrique, bourse, sika finance',
    packages=find_packages(exclude=['tests', 'docs', 'examples']),
    install_requires=[
        'pandas>=1.0.0',
        'requests>=2.20.0'
    ],
    include_package_data=True,
)

# --- Le Disclaimer (Très important quand on fait du Web Scraping) ---
print("""
====================================================================
NOTE: `brvmfinance` n'est pas affilié, soutenu ou validé par la
BRVM (Bourse Régionale des Valeurs Mobilières) ni par SikaFinance.

Cet outil est fourni à des fins éducatives et de recherche.
Vous devez vous référer aux conditions d'utilisation des sources
d'origine concernant vos droits d'utilisation des données téléchargées.
====================================================================
""")
