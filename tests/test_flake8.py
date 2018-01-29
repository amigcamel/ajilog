"""Test flake8."""
import os

from . import ROOT


def test_flake8():
    """Test flake8 (check PEP)."""
    assert os.system('flake8 %s' % ROOT) == 0
