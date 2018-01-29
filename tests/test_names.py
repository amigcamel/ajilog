"""Test logger names."""
from io import StringIO

from ajilog import logger


def test_names():
    """Test if logger name conform to script name."""
    buffer = StringIO()
    logger.stream = buffer
    logger.debug(u'')
    output = buffer.getvalue()
    buffer.close()
    assert __file__.split('/')[-1].split('.py')[0] in output
