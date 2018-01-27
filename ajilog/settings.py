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

    name = None

    def __init__(self):
        """Create dict to store loggers."""
        self._loggers = {}

    def __getattr__(self, name):
        """Get attribute of self."""
        logger_name = self.name or self.filename
        if name == 'name':
            return logger_name
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

    def __repr__(self):
        """Make human-readable."""
        return str(self._loggers)

    @property
    def filename(self):
        filepath = getfile(currentframe().f_back.f_back)
        fname = filepath.split('/')[-1].replace('.py', '')
        if 'ipython-input-' in fname:
            fname = 'ipython-input'
        return fname

    def replace_print(self, log_level='debug'):
        """Replace built-in `print` function with logger."""
        import builtins
        builtins.print = getattr(self, log_level)


logger = _Logger()
