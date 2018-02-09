"""Test logger names."""
from io import StringIO

from .conf import import_ajilog


def test_names():
    """Test if logger name conform to script name."""
    logger = import_ajilog().logger
    logger.stream = StringIO()
    logger.debug(u'')
    assert __file__.split('/')[-1].split('.py')[0] in logger.stream.getvalue()
