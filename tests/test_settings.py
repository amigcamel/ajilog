"""Test settings."""
from uuid import uuid4
from os.path import isdir, join
from tempfile import gettempdir
from shutil import rmtree

from six.moves import reload_module

from .conf import import_ajilog


def test_settings(monkeypatch):
    """Test rotate-related settings."""
    ajilog = import_ajilog()

    reload_module(ajilog.settings)

    monkeypatch.setitem(ajilog.settings.config['rotate'], 'enable', 'true')
    monkeypatch.setitem(ajilog.settings.config['rotate'],
                        'dir', join(gettempdir(), uuid4().hex))
    monkeypatch.setitem(ajilog.settings.config['rotate'], 'level', 'debug')

    ajilog.logger.debug(u'')
    assert isdir(ajilog.settings.ROTATE_DIR)
    rmtree(ajilog.settings.ROTATE_DIR)
