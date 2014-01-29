import doctest
from six import print_
from unicodecsv.test_deps import unittest


def get_suite():
    loader = unittest.TestLoader()
    suite = loader.discover('unicodecsv')
    suite.addTest(doctest.DocTestSuite('unicodecsv'))
    return suite


if __name__ == '__main__':
    result = unittest.TestResult()
    get_suite().run(result)
    for error in result.errors:
        print_(error)
