"""Test logger names."""
from ajilog import logger


def test_names():
    """Test if logger name conform to script name."""
    logger.stream.truncate(0)
    logger.debug(u'')
    assert __file__.split('/')[-1].split('.py')[0] in logger.stream.getvalue()
