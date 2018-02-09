"""Logging configurations."""
from inspect import currentframe, getfile
from os.path import join, exists
from os import mkdir
from logging.handlers import TimedRotatingFileHandler
import logging

from colorlog import ColoredFormatter

from . import settings


class _Logger():
    """Logger object."""

    datefmt = '%y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(
        (
            '%(levelname)-5s '
            '[%(asctime)s] '
            '%(name)s %(funcName)s '
            ':%(lineno)d '
            '%(message)s'
        ),
        datefmt=datefmt,
    )

    colored_formatter = ColoredFormatter(
        (
            '%(log_color)s%(levelname)-5s%(reset)s '
            '%(yellow)s[%(asctime)s]%(reset)s%(white)s '
            '%(name)s %(funcName)s '
            '%(bold_purple)s:%(lineno)d%(reset)s '
            '%(log_color)s%(message)s%(reset)s'
        ),
        datefmt=datefmt,
        log_colors={
            'DEBUG': 'blue',
            'INFO': 'bold_cyan',
            'WARNING': 'red,',
            'ERROR': 'bg_bold_red',
            'CRITICAL': 'red,bg_white',
        }
    )

    stream = None
    use_color = True

    def __init__(self, stream=None):
        """Create dict to store loggers."""
        logging.getLogger().setLevel(logging.DEBUG)
        self._loggers = logging.Logger.manager.loggerDict
        self._loggers.clear()  # clear all existed loggers

    def __getattr__(self, name):
        """Get attribute of self."""
        logger_name = self.get_current_file('name')
        # print('try to find logger: ', logger_name)
        if not self._loggers.get(logger_name):
            # print('logger ', logger_name, 'not found, now set_stream')
            self.set_stream()
            if settings.ROTATE_ENABLE:
                self.set_rotate()
            # print('loggerDict: ', logging.Logger.manager.loggerDict)
        return getattr(self._loggers[logger_name], name)

    def set_stream(self):
        """Set formatter and add handlers."""
        logger_name = self.get_current_file('name')
        _logger = logging.getLogger(logger_name)
        _logger.setLevel(logging.DEBUG)

        sh = logging.StreamHandler(self.stream)
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(
            self.colored_formatter if self.use_color else self.formatter)
        _logger.addHandler(sh)

    def set_rotate(self, log_level=None, log_dir=None):
        """Use TimedRotatingFileHandler."""
        log_level = settings.ROTATE_LEVEL or 'DEBUG'
        log_dir = settings.ROTATE_DIR or '/tmp/logs'
        logger_name = self.get_current_file('name')
        if not exists(log_dir):
            mkdir(log_dir)
        # check if log_dir exists
        fh = TimedRotatingFileHandler(
            join(log_dir, logger_name),
            when='midnight',
            backupCount=7
        )
        fh.setLevel(log_level)
        fh.setFormatter(self.formatter)
        # print('logger_name: ', logger_name)
        logging.getLogger(logger_name).addHandler(fh)

    def __repr__(self):
        """Make human-readable."""
        return str(self._loggers)

    def get_current_file(self, target):
        """Get current file info.

        parameters:
        - target: 'name' or 'path'

        """
        assert target in ('name', 'path')
        frame = currentframe()
        while True:
            filepath = getfile(frame)
            if __file__ == filepath:
                frame = frame.f_back
            elif 'ipython-input-' in filepath:
                filepath = getfile(frame.f_back)
                break
            else:
                break
        # print('----------', filepath, '-------------')
        if target == 'path':
            return filepath
        elif target == 'name':
            return filepath.split('/')[-1].split('.py')[0]


logger = _Logger()
