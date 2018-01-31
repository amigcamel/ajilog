"""Test escape codes."""
from ajilog import logger


def test_with_color():
    """Test if color displays."""
    logger.stream.truncate(0)
    logger.debug(u'')
    assert '\x1b[' in logger.stream.getvalue()


def test_without_color():
    """Test if color not displays."""
    logger._loggers.pop(logger.filename)
    logger.use_color = False
    logger.stream.truncate(0)
    logger.debug(u'')
    assert '\x1b[' not in logger.stream.getvalue()
