from mako.template import Template
from mako.lookup import TemplateLookup
import os

class Service(object):
    DEFAULT_OPTIONS = ["template.path"]

    def __init__(self, conf):
        self.conf = conf
        self.lookup = TemplateLookup(directories=[self.conf["template.path"]], output_encoding='utf-8')

    def configure(self, k, v):
        self.conf[k] = v

    def get_template(self, filename):
        return self.lookup.get_template(filename)
