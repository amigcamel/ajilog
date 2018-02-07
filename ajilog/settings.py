"""Settings."""
import os
from distutils.util import strtobool

USE_ROTATE = strtobool(os.environ.get('AJILOG_USE_ROTATE', 'False'))
