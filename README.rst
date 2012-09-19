unicodecsv
==========

The unicodecsv is a drop-in replacement for Python 2's csv module which supports unicode strings without a hassle.

More fully
----------

Python 2's csv module doesn't easily deal with unicode strings, leading to the dreaded "'ascii' codec can't encode characters in position ..." exception.

You can work around it by encoding everything just before calling write (or just after read), but why not add support to the serializer?

::

   >>> import unicodecsv
   >>> from cStringIO import StringIO
   >>> f = StringIO()
   >>> w = unicodecsv.writer(f, encoding='utf-8')
   >>> w.writerow((u'é', u'ñ'))
   >>> f.seek(0)
   >>> r = unicodecsv.reader(f, encoding='utf-8')
   >>> row = r.next()
   >>> print row[0], row[1]
   é ñ
