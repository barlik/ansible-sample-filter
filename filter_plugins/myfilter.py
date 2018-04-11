from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2 import Environment, FileSystemLoader
from ansible import errors

def myfilter(*args):
    return ''.join(arg[::-1] for arg in args)

class FilterModule(object):
     def filters(self):
         return {
             'myfilter': myfilter
         }
