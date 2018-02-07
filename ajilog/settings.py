"""Settings."""
import os
from distutils.util import strtobool


ROTATE_ENABLE = strtobool(os.environ.get('ROTATE_ENABLE', 'False'))
ROTATE_LEVEL = os.environ.get('ROTATE_LEVEL')
ROTATE_DIR = os.environ.get("ROTATE_DIR")
