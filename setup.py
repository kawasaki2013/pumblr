from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='pumblr',
      version=version,
      description="A python library for The Tumblr API.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='tumblr',
      author='seikichi',
      author_email='seikichi@kmc.gr.jp',
      url='http://d.hatena.ne.jp/se-kichi',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )