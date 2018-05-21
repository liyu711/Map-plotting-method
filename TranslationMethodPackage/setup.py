# This is the setup file for pip
from setuptools import setup, find_packages
import os, sys
from os import path

setup(name='TranslationMethod',

      version='0.1',

      description='Translate Depth Map into 3D map',

      url='https://github.com/liyu711/Map-plotting-method.git',

      author='Yudong Li',

      author_email='a1923172548@gmail.com',

      license='MIT',

      install_requires = ['numpy'],

      packages=find_packages(),

      zip_safe=False)