"""Logging configurations."""
from inspect import currentframe, getfile
from os.path import join
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
            '%(log_color)s%(levelname)-8s%(reset)s '
            '%(yellow)s[%(asctime)s]%(reset)s%(white)s '
            '%(name)s %(funcName)s '
            '%(bold_purple)s:%(lineno)3d%(reset)s '
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

    def __init__(self, stream=None):
        """Create dict to store loggers."""
        logging.getLogger().setLevel(logging.DEBUG)

    def __getattr__(self, name):
        """Get attribute of self."""
        logger_name = self.get_current_name()
        if not logging.Logger.manager.loggerDict.get(logger_name):
            self.set_stream()
            if settings.ROTATE_ENABLE:
                self.set_rotate()
        return getattr(logging.Logger.manager.loggerDict[logger_name], name)

    def set_stream(self):
        """Set formatter and add handlers."""
        logger_name = self.get_current_name()
        _logger = logging.getLogger(logger_name)
        _logger.propagate = False

        sh = logging.StreamHandler(self.stream)
        sh.setLevel(settings.STREAM_LEVEL)
        sh.setFormatter(self.colored_formatter
                        if settings.STREAM_COLOR
                        else self.formatter)
        _logger.addHandler(sh)

    def set_rotate(self):
        """Use TimedRotatingFileHandler."""
        logger_name = self.get_current_name()
        # check if log_dir exists
        fh = TimedRotatingFileHandler(
            join(settings.ROTATE_DIR, logger_name),
            when='midnight',
            backupCount=7
        )
        fh.setLevel(settings.ROTATE_LEVEL)
        fh.setFormatter(self.formatter)
        _logger = logging.getLogger(logger_name)
        _logger.propagate = False
        _logger.addHandler(fh)

    def __repr__(self):
        """Make human-readable."""
        return str(logging.Logger.manager.loggerDict)

    def get_current_name(self):
        """Get current file info."""
        frame = currentframe()
        while __file__ == getfile(frame):
            frame = frame.f_back
        if getfile(frame).endswith('__init__.py'):
            frame = frame.f_back
        logger_name = frame.f_globals.get(
            '__loggername__', frame.f_globals['__name__'])
        return logger_name


logger = _Logger()
