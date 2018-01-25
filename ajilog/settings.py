"""Logging configurations."""
import logging
import inspect

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
        return getattr(self._log, name)

    def __setattr__(self, name, val):
        if name == 'name':
            setattr(self._log, name, val)
        else:
            super().__setattr__(name, val)

    def __repr__(self):
        """Make human-readable."""
        return str(self._loggers)

    @property
    def _log(self):

        filename, *_ = inspect.getframeinfo(
            inspect.currentframe().f_back.f_back.f_back
        )
        name = filename.split('/')[-1].split('.py')[0]
        if self._loggers.get(name):
            return self._loggers.get(name)

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # StreamHandler
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(self.formatter)

        # Add handlers
        logger.addHandler(sh)
        self._loggers[name] = logger
        return logger


logger = _Logger()
