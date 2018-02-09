"""Configurations."""
import importlib

import pytest


@pytest.fixture(scope='module')
def import_ajilog():
    """Import ajilog."""
    return importlib.import_module('ajilog')
