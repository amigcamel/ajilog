"""Logging configurations."""
import logging
import sys

from colorlog import ColoredFormatter

from . import settings


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


class initialize:
    """Call this function to patch the default root logger."""

    def __init__(self):
        """Patch root loggers."""
        sh = logging.StreamHandler()
        sh.setFormatter(ColoredFormatter(settings.LOG_FORMAT,
                                         datefmt=settings.DATE_FORMAT,
                                         log_colors=settings.LOG_COLORS))
        logging.root.setLevel(logging.DEBUG)
        logging.root.addHandler(sh)
        logging.debug('ajilog initialized')
