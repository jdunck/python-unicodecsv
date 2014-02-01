import doctest
from six import print_
from unicodecsv.test_deps import unittest, old


def get_suite():
    loader = unittest.TestLoader()
    suite = loader.discover('unicodecsv')
    if old:
        suite.addTest(doctest.DocTestSuite('unicodecsv.two'))
    return suite


if __name__ == '__main__':
    result = unittest.TestResult()
    get_suite().run(result)
    for error in result.errors:
        print_(error)
