"""Settings."""
from os.path import join, exists
from tempfile import gettempdir
import json

CONF_NAME = 'ajilog.json'

HANDLERS = {
    'STREAM': {
        'datefmt': '%y-%m-%d %H:%M:%S',
        'enabled': True,
        'format': '%(log_color)s%(levelname)-8s%(reset)s %(yellow)s[%(asctime)s]%(reset)s%(white)s %(name)s %(funcName)s %(bold_purple)s:%(lineno)3d%(reset)s %(log_color)s%(message)s%(reset)s',  # noqa: E501
        'level': 'DEBUG',
        'log_colors': {
            'DEBUG': 'blue',
            'INFO': 'bold_cyan',
            'WARNING': 'blue,red,',
            'ERROR': 'bg_bold_red',
            'CRITICAL': 'red,bg_white',
        }
    },
    'FILE': {
        'datefmt': '%y-%m-%d %H:%M:%S',
        'enabled': False,
        'format': '%(levelname)-5s [%(asctime)s] %(name)s %(funcName)s :%(lineno)d %(message)s',  # noqa: E501
        'level': 'INFO',
        'path': join(gettempdir(), 'ajilog.log'),
    },
    'TIME_ROTATE': {
        'backupCount': 7,
        'datefmt': '%y-%m-%d %H:%M:%S',
        'enabled': False,
        'format': '%(levelname)-5s [%(asctime)s] %(name)s %(funcName)s :%(lineno)d %(message)s',  # noqa: E501
        'level': 'INFO',
        'path': join(gettempdir(), 'ajilog_trh.log'),  # TODO: ensure dir exist
        'when': 'midnight',
    },
}

if exists(CONF_NAME):
    with open(CONF_NAME) as f:
        HANDLERS = json.load(f)
