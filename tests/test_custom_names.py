"""Test logger names."""
from io import StringIO

from .conf import import_ajilog

test_str = 'test_logger_name'
__loggername__ = test_str

logger = import_ajilog().logger
logger.stream = StringIO()
logger.debug(u'')
assert test_str in logger.stream.getvalue()
