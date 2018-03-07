"""Settings."""
from distutils.util import strtobool
from configparser import ConfigParser
from distutils import dir_util
from os.path import exists, join
from tempfile import gettempdir

config = ConfigParser()
config.read('ajilog.conf')

# stream
STREAM_COLOR = strtobool(config.get('stream', 'color', fallback='true'))
STREAM_LEVEL = config.get('stream', 'level', fallback='debug').upper()

# rotate
ROTATE_ENABLE = strtobool(config.get('rotate', 'enable', fallback='false'))
ROTATE_LEVEL = config.get('rotate', 'level', fallback='debug').upper()
ROTATE_DIR = config.get('rotate', 'dir', fallback=join(gettempdir(), 'logs'))
if ROTATE_ENABLE and (not exists(ROTATE_DIR)):
    dir_util.mkpath(ROTATE_DIR)
    print('rotating dir created: %s' % ROTATE_DIR)
