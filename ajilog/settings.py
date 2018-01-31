"""Logging configurations."""
from inspect import currentframe, getfile
import logging

from colorlog import ColoredFormatter


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

    name = None
    stream = None
    use_color = True

    def __init__(self, stream=None):
        """Create dict to store loggers."""
        self._loggers = logging.Logger.manager.loggerDict

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
            sh = logging.StreamHandler(self.stream)
            sh.setLevel(logging.DEBUG)
            sh.setFormatter(
                self.colored_formatter if self.use_color else self.formatter)

            # Add handlers
            logger.addHandler(sh)
            self._loggers[logger_name] = logger
        return getattr(logger, name)

    def __repr__(self):
        """Make human-readable."""
        return str(self._loggers)

    @property
    def filename(self):
        frame = currentframe()
        filepath = getfile(frame.f_back.f_back)
        if 'ipython-input-' in filepath:
            filepath = getfile(frame.f_back.f_back.f_back)
        if '_pytest' in filepath:
            filepath = getfile(frame.f_back)
        fname = filepath.split('/')[-1].replace('.py', '')
        return fname


logger = _Logger()
