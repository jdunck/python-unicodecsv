import unittest2
import doctest

def get_suite():
    loader = unittest2.TestLoader()
    suite = loader.discover('unicodecsv')
    suite.addTest(doctest.DocTestSuite('unicodecsv'))

    return suite

if __name__ == '__main__':
    get_suite().run()
