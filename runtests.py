import unittest2
import doctest

def get_suite():
    loader = unittest2.TestLoader()
    suite = loader.discover('unicodecsv')
    suite.addTest(doctest.DocTestSuite('unicodecsv'))

    return suite

if __name__ == '__main__':
    result = unittest2.TestResult()
    get_suite().run(result)
    for error in result.errors:
        print error
