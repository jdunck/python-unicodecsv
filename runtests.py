import sys
import unittest2
import doctest

def get_suite():
    # no tests under python 3 since we simply defer to the vanilla module.
    if sys.version_info >= (3, 0):
        return unittest2.TestSuite()

    loader = unittest2.TestLoader()
    suite = loader.discover('unicodecsv.py2')
    suite.addTest(doctest.DocTestSuite('unicodecsv.py2'))

    return suite

def main():
    result = unittest2.TestResult()
    get_suite().run(result)
    for error in result.errors:
        print(error)

if __name__ == '__main__':
    main()