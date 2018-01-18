import sys
import unittest
import doctest

def get_suite():
    if sys.version_info >= (3, 0):
        start_module = 'unicodecsv.py3'
    else:
        start_module = 'unicodecsv.py2'

    loader = unittest.TestLoader()
    suite = loader.discover(start_module)
    suite.addTest(doctest.DocTestSuite(start_module))
    suite.addTest(doctest.DocFileSuite('README.rst', optionflags=doctest.ELLIPSIS))

    return suite

def main():
    result = unittest.TestResult()
    get_suite().run(result)
    for error in result.errors:
        print(error)

if __name__ == '__main__':
    main()
