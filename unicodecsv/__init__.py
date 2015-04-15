# -*- coding: utf-8 -*-
#http://semver.org/
VERSION = (0, 12, 0)
__version__ = ".".join(map(str,VERSION))

import sys

if sys.version_info >= (3, 0):
    from unicodecsv.py3 import *
else:
    from unicodecsv.py2 import *
