#!/usr/bin/env python

from setuptools import setup

setup(name='prototype_analytical_core',
      version='0.1',
      description='The analytical core processes incoming requests for data processing using predictive analysis '
                  'methods. The result of the work is a JSON package with the results of the analysis. A packet with '
                  'the result is sent to the client from which the data came.',
      author='Osintsev Artem',
      author_email='artem.osintsev@innovacia.ru',
      url='https://infomatix.pro',
      install_requires=[
          'fastapi',
          'uvicorn',
          'SQLAlchemy',
          'pytest',
          'requests'],
      scripts=['scripts/create_db.py', 'app/main.py']
      )
