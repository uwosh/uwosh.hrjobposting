# -*- coding: utf-8 -*-
"""
This module contains the tool of uwosh.hrjobposting
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0.4.2'

long_description = (
    read('README.txt')
    + '\n' +
    '********\n')

tests_require = ['zope.testing']

setup(name='uwosh.hrjobposting',
      version=version,
      description="Human Resources Job Posting",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='HR,Job posting',
      author='Joel Herron',
      author_email='herronj@uwosh.edu',
      url='http://www.uwosh.edu/ploneprojects/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uwosh', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='uwosh.hrjobposting.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # setup_requires=["PasteScript"],
      # paster_plugins=["ZopeSkel"],
      )
