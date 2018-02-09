"""Test settings."""
import os
from uuid import uuid4
from os.path import isdir, join
from tempfile import gettempdir
from shutil import rmtree

from six.moves import reload_module

from .conf import import_ajilog


def test_settings(monkeypatch):
    """Test rotate-related settings."""
    monkeypatch.setenv('ROTATE_ENABLE', 'true')
    monkeypatch.setenv('ROTATE_DIR', join(gettempdir(), uuid4().hex))
    monkeypatch.setenv('ROTATE_LEVEL', 'DEBUG')

    ajilog = import_ajilog()

    reload_module(ajilog.settings)

    ajilog.logger.debug(u'')
    assert isdir(os.environ['ROTATE_DIR'])
    rmtree(os.environ['ROTATE_DIR'])
