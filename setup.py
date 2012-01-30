import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
requires = [
    "webob",
    "webdispatch", 
    "webtest", 
    "mako", 
    "fanstatic"
    ]

setup(name='runningwheel',
      version='0.0',
      packages=find_packages(), 
      install_requires=requires,
      )
