import sys
import unittest2
import doctest

def get_suite():
    if sys.version_info >= (3, 0):
        start_module = 'unicodecsv.py3'
    else:
        start_module = 'unicodecsv.py2'

    loader = unittest2.TestLoader()
    suite = loader.discover(start_module)
    suite.addTest(doctest.DocTestSuite(start_module))

    return suite

def main():
    result = unittest2.TestResult()
    get_suite().run(result)
    for error in result.errors:
        print(error)

if __name__ == '__main__':
    main()