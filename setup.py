#!/usr/bin/env python

from distutils.core import setup

setup(name='paypal_auth_headers',
      version='1.0',
      descrition='Generate signature for header in PayPal api calls',
      # im not the author, im just porting this
      author="Piotr Szymanski",
      author_email="p.szymanski@bidpy.pl",
      url="https://github.com/eddwardo/python-signature-generator-for-authentication-header",
      packages=['paypal_auth_header'],
)
