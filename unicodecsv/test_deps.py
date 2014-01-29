import sys
old = sys.version_info[0] < 3

if old:
    import unittest2 as unittest
    from StringIO import StringIO
    from string import letters
else:
    import unittest
    from io import StringIO
    from string import ascii_letters as letters
