import sys

if sys.version_info[0] < 3:
    import unittest2 as unittest
    from StringIO import StringIO
else:
    import unittest
    from io import StringIO
