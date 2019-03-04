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


STREAM = {
    'datefmt': '%y-%m-%d %H:%M:%S',
    'format': '%(log_color)s%(levelname)-8s%(reset)s %(yellow)s[%(asctime)s]%(reset)s%(white)s %(name)s %(funcName)s %(bold_purple)s:%(lineno)3d%(reset)s %(log_color)s%(message)s%(reset)s',  # noqa: E501
    'log_colors': {
        'DEBUG': 'blue',
        'INFO': 'bold_cyan',
        'WARNING': 'red,',
        'ERROR': 'bg_bold_red',
        'CRITICAL': 'red,bg_white',
    }
}

FILE = {
    'datefmt': '%y-%m-%d %H:%M:%S',
    'format': '%(levelname)-5s [%(asctime)s] %(name)s %(funcName)s :%(lineno)d %(message)s',  # noqa: E501
    'level': 'INFO',
    'path': join(gettempdir(), 'ajilog.log'),
}

TIME_ROTATE = {
    'backupCount': 7,
    'datefmt': '%y-%m-%d %H:%M:%S',
    'format': '%(levelname)-5s [%(asctime)s] %(name)s %(funcName)s :%(lineno)d %(message)s',  # noqa: E501
    'level': 'INFO',
    'path': join(gettempdir(), 'ajilog_trh.log'),  # TODO: ensure dir exist
    'when': 'midnight',
}
