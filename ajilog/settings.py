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


DATE_FORMAT = '%y-%m-%d %H:%M:%S'
LOG_FORMAT = '%(log_color)s%(levelname)-8s%(reset)s %(yellow)s[%(asctime)s]%(reset)s%(white)s %(name)s %(funcName)s %(bold_purple)s:%(lineno)3d%(reset)s %(log_color)s%(message)s%(reset)s'  # noqa: E501
LOG_COLORS = {
    'DEBUG': 'blue',
    'INFO': 'bold_cyan',
    'WARNING': 'red,',
    'ERROR': 'bg_bold_red',
    'CRITICAL': 'red,bg_white',
}
