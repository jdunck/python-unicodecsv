unicodecsv
==========

The unicodecsv is a drop-in replacement for Python 2.7's csv module which supports unicode strings without a hassle.  Supported versions are python 2.6, 2.7, 3.3, 3.4, 3.5, and pypy 2.4.0.

More fully
----------

Python 2's csv module doesn't easily deal with unicode strings, leading to the dreaded "'ascii' codec can't encode characters in position ..." exception.

You can work around it by encoding everything just before calling write (or just after read), but why not add support to the serializer?

.. code-block:: pycon

   >>> import unicodecsv as csv
   >>> from io import BytesIO
   >>> f = BytesIO()
   >>> w = csv.writer(f, encoding='utf-8')
   >>> _ = w.writerow((u'é', u'ñ'))
   >>> _ = f.seek(0)
   >>> r = csv.reader(f, encoding='utf-8')
   >>> next(r) == [u'é', u'ñ']
   True

Note that unicodecsv expects a bytestream, not unicode -- so there's no need to use `codecs.open` or similar wrappers.  Plain `open(..., 'rb')` will do.

(Version 0.14.0 dropped support for python 2.6, but 0.14.1 added it back.  See c0b7655248c4249 for the mistaken, breaking change.)

Python 3 Magic
--------------

In order to make ``unicodecsv`` a drop-in replacement for Python 3's built-in module, we had to do something clever. If the ``encoding`` argument is present, then the file is assumed to be in binary mode. If the ``encoding`` argument is not present and we are using Python 3, then ``unicodecsv`` will fall back to the behavior of Python 3's built-in ``csv`` module, which is to read and write text, not bytes.
