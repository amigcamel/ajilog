"""Logging configurations."""
from inspect import currentframe, getfile
import logging

from colorlog import ColoredFormatter


class _Logger():
    """Logger object."""

    formatter = ColoredFormatter(
        (
            '%(log_color)s%(levelname)-5s%(reset)s '
            '%(yellow)s[%(asctime)s]%(reset)s%(white)s '
            '%(name)s %(funcName)s '
            '%(bold_purple)s:%(lineno)d%(reset)s '
            '%(log_color)s%(message)s%(reset)s'
        ),
        datefmt='%y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'blue',
            'INFO': 'bold_cyan',
            'WARNING': 'red,',
            'ERROR': 'bg_bold_red',
            'CRITICAL': 'red,bg_white',
        }
    )

    def __init__(self):
        """Create dict to store loggers."""
        self._loggers = {}

    def __getattr__(self, name):
        """Get attribute of self."""
        filepath = getfile(currentframe().f_back)
        logger_name = filepath.split('/')[-1].replace('.py', '')
        if self._loggers.get(logger_name):
            logger = self._loggers.get(logger_name)
        else:
            logger = logging.getLogger(logger_name)
            logger.setLevel(logging.DEBUG)

            # StreamHandler
            sh = logging.StreamHandler()
            sh.setLevel(logging.DEBUG)
            sh.setFormatter(self.formatter)

            # Add handlers
            logger.addHandler(sh)
            self._loggers[logger_name] = logger
        return getattr(logger, name)

    def __setattr__(self, name, val):
        if name == 'name':
            setattr(self._log, name, val)
        else:
            super().__setattr__(name, val)

    def __repr__(self):
        """Make human-readable."""
        return str(self._loggers)


logger = _Logger()
