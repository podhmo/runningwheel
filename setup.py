import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
requires = [
    "webob",
    "webdispatch", 
    "webtest", 
    "mako", 
    "fanstatic", 
    "js.json2",
    "js.underscore", 
    "js.jquery", 
    "js.jquery_tools", 
    "js.jqueryui"
    ]

setup(name='runningwheel',
      version='0.0',
      packages=find_packages(), 
      install_requires=requires,
      )
