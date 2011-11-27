# -*- coding: utf-8 -*-
import csv

#http://semver.org/
VERSION = (0, 8, 0)
__version__ = ".".join(map(str,VERSION))

pass_throughs = [
    'register_dialect',
    'unregister_dialect',
    'get_dialect',
    'list_dialects',
    'field_size_limit',
    'Dialect',
    'excel',
    'excel_tab',
    'Sniffer',
    'QUOTE_ALL',
    'QUOTE_MINIMAL',
    'QUOTE_NONNUMERIC',
    'QUOTE_NONE',
    'Error'
]
__all__ = [
    'reader',
    'writer',
    'DictReader',
    'DictWriter',
] + pass_throughs

for prop in pass_throughs:
    globals()[prop]=getattr(csv, prop)

def _stringify(s, encoding):
    if s is None:
        return ''
    if type(s)==unicode:
        return s.encode(encoding)
    elif isinstance(s, (int , float)):
        pass #let csv.QUOTE_NONNUMERIC do its thing.
    elif type(s) != str:
        s=str(s)
    return s

def _stringify_list(l, encoding):
    try:
        return [_stringify(s, encoding) for s in iter(l)]
    except TypeError:
        raise csv.Error()

class UnicodeWriter(object):
    """
    >>> import unicodecsv
    >>> from cStringIO import StringIO
    >>> f = StringIO()
    >>> w = unicodecsv.writer(f, encoding='utf-8')
    >>> w.writerow((u'é', u'ñ'))
    >>> f.seek(0)
    >>> r = unicodecsv.reader(f, encoding='utf-8')
    >>> row = r.next()
    >>> row[0] == u'é'
    True
    >>> row[1] == u'ñ'
    True
    """
    def __init__(self, f, dialect=csv.excel, encoding="utf-8", *args, **kwds):
        self.encoding = encoding
        self.writer = csv.writer(f, dialect, *args, **kwds)

    def writerow(self, row):
        self.writer.writerow(_stringify_list(row, self.encoding))

    def writerows(self, rows):
        for row in rows:
          self.writerow(row)

    @property
    def dialect(self):
        return self.writer.dialect
writer = UnicodeWriter

class UnicodeReader(object):
    def __init__(self, f, dialect=None, encoding="utf-8", **kwds):
        format_params = ['delimiter', 'doublequote', 'escapechar', 'lineterminator', 'quotechar', 'quoting', 'skipinitialspace']
        if dialect is None:
            if not any([kwd_name in format_params for kwd_name in kwds.keys()]):
                dialect = csv.excel
        self.reader = csv.reader(f, dialect, **kwds)
        self.encoding = encoding

    def next(self):
        row = self.reader.next()
        results = []
        for value in row:
            if isinstance(value, float):
                results.append(value)
            else:
                results.append(unicode(value, self.encoding))
        return results

    def __iter__(self):
        return self

    @property
    def dialect(self):
        return self.reader.dialect

    @property
    def line_num(self):
        return self.reader.line_num
reader = UnicodeReader

class DictWriter(csv.DictWriter):
    """
    >>> from cStringIO import StringIO
    >>> f = StringIO()
    >>> w = DictWriter(f, ['a', 'b'], restval=u'î')
    >>> w.writerow({'a':'1'})
    >>> w.writerow({'a':'1', 'b':u'ø'})
    >>> w.writerow({'a':u'é'})
    >>> f.seek(0)
    >>> r = DictReader(f, fieldnames=['a'], restkey='r')
    >>> print r.next() == {'a': u'1', 'r': [u'î']}
    True
    >>> print r.next() == {'a': u'1', 'r': [u'\xc3\xb8']}
    True
    >>> print r.next() == {'a': u'\xc3\xa9', 'r': [u'\xc3\xae']}
    True
    """
    def __init__(self, csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', encoding='utf-8', *args, **kwds):
        csv.DictWriter.__init__(self, csvfile, fieldnames, restval, extrasaction, dialect, *args, **kwds)
        self.writer = UnicodeWriter(csvfile, dialect, encoding=encoding, *args, **kwds)

    def writeheader(self):
        header = dict(zip(self.fieldnames, self.fieldnames))
        self.writerow(header)

class DictReader(csv.DictReader):
    """
    >>> from cStringIO import StringIO
    >>> f = StringIO()
    >>> w = DictWriter(f, fieldnames=['name', 'place'])
    >>> w.writerow({'name': 'Cary Grant', 'place': 'hollywood'})
    >>> w.writerow({'name': 'Nathan Brillstone', 'place': u'øLand'})
    >>> w.writerow({'name': u'Willam ø. Unicoder', 'place': u'éSpandland'})
    >>> f.seek(0)
    >>> r = DictReader(f, fieldnames=['name', 'place'])
    >>> print r.next() == {'name': 'Cary Grant', 'place': 'hollywood'}
    True
    >>> print r.next() == {'name': 'Nathan Brillstone', 'place': u'øLand'}
    True
    >>> print r.next() == {'name': u'Willam ø. Unicoder', 'place': u'éSpandland'}
    True
    """
    def __init__(self, csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', encoding='utf-8', *args, **kwds):
        csv.DictReader.__init__(self, csvfile, fieldnames, restkey, restval, dialect, *args, **kwds)
        self.reader = UnicodeReader(csvfile, dialect, encoding=encoding, *args, **kwds)
