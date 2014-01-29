#http://semver.org/
VERSION = (0, 10, 1)
__version__ = ".".join(map(str,VERSION))
import csv

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

import sys
if sys.version_info[0] < 3:
	from two import reader, writer, DictReader, DictWriter
else:
	from csv import reader, writer, DictReader, DictWriter
