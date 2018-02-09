"""Test escape codes."""
from io import StringIO

from .conf import import_ajilog


def test_with_color():
    """Test if color displays."""
    logger = import_ajilog().logger
    logger.stream = StringIO()
    logger.debug(u'')
    assert '\x1b[' in logger.stream.getvalue()


def test_without_color():
    """Test if color not displays."""
    logger = import_ajilog().logger
    logger.stream = StringIO()
    logger.use_color = False
    logger.debug(u'')
    assert '\x1b[' not in logger.stream.getvalue()
