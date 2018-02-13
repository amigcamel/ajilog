"""Test __repr__."""
import logging

from .conf import import_ajilog


def test_repr():
    """Test logger repr."""
    logger = import_ajilog().logger
    assert logger.__repr__() == str(logging.Logger.manager.loggerDict)
