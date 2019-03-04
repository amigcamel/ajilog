"""Logging configurations."""
import logging
import sys

from colorlog import ColoredFormatter


datefmt = '%y-%m-%d %H:%M:%S'
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


class AjiLogRecord(logging.LogRecord):
    """Custom LogRecord."""

    def __init__(self, *args, **kwargs):
        """Add `qualname`."""
        frame = sys._getframe()
        # TODO: add comments
        while frame.f_globals['__package__'] != 'logging':
            frame = frame.f_back
        while frame.f_globals['__package__'] == 'logging':
            frame = frame.f_back
        qualname = frame.f_globals['__name__']
        # TODO: add comments
        logging.Logger.manager.getLogger(qualname)
        # TODO: add comments
        patched_args = []
        patched_args.append(qualname)
        patched_args.extend(args[1:])
        args = tuple(patched_args)
        super().__init__(*args, **kwargs)


logging._logRecordFactory = AjiLogRecord


class initialize(logging.Logger):
    """Logger object."""

    def __init__(self, *args, **kwargs):
        """Create dict to store loggers."""
        super().__init__(self, *args, **kwargs)
        sh = logging.StreamHandler()
        sh.setFormatter(colored_formatter)
        logger = logging.getLogger()
        logger.propagate = False
        logger.setLevel(logging.DEBUG)
        logger.addHandler(sh)
        self.logger = logger
