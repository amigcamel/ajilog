"""Test settings."""
from os.path import isdir
from shutil import rmtree

from .conf import import_ajilog


def test_settings():
    """Test rotate-related settings."""
    ajilog = import_ajilog()

    ajilog.logger.debug(u'')
    assert isdir(ajilog.settings.ROTATE_DIR)
    rmtree(ajilog.settings.ROTATE_DIR)
