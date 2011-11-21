import unittest2

def get_suite():
    loader = unittest2.TestLoader()
    suite = loader.discover('unicodecsv')
    return suite

if __name__ == '__main__':
    get_suite().run()
