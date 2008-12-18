# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2007, Agendaless Consulting and Contributors.
# Copyright (c) 2008, Florent Aide <florent.aide@gmail.com> and
#                     Gustavo Narea <me@gustavonarea.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

import os

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
version = open(os.path.join(here, 'VERSION.txt')).readline().rstrip()

setup(name='repoze.who.plugins.sqlalchemy',
      version=version,
      description=('The repoze.who SQLAlchemy plugin'),
      long_description=README,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        ],
      keywords='web application server wsgi sql sqlalchemy elixir',
      author="Gustavo Narea",
      author_email="repoze-dev@lists.repoze.org",
      namespace_packages=['repoze', 'repoze.who', 'repoze.who.plugins'],
      url="http://code.gustavonarea.net/repoze.who.plugins.sqlalchemy/",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require=[
          'repoze.who',
          'coverage',
          'nose',
          'sqlalchemy >= 0.5.0rc4',
          'elixir'],
      install_requires=['repoze.who', 'sqlalchemy >= 0.5.0rc4'],
      test_suite="nose.collector",
      entry_points = """\
      """
      )
