"""Logging configurations."""
import logging
import logging.handlers
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
        # stream handler
        sh = logging.StreamHandler()
        sh.setFormatter(ColoredFormatter(
            settings.STREAM['format'],
            datefmt=settings.STREAM['datefmt'],
            log_colors=settings.STREAM['log_colors']))
        logging.root.setLevel(logging.DEBUG)
        logging.root.addHandler(sh)

        # file handler
        fh = logging.FileHandler(settings.FILE['path'])
        fh.setLevel(getattr(logging, settings.FILE['level']))
        fh.setFormatter(logging.Formatter(
            settings.FILE['format'], settings.FILE['datefmt']))
        logging.root.addHandler(fh)

        # rotating file handler
        trh = logging.handlers.TimedRotatingFileHandler(
            settings.TIME_ROTATE['path'],
            when=settings.TIME_ROTATE['when'],
            backupCount=settings.TIME_ROTATE['backupCount'])
        trh.setLevel(getattr(logging, settings.TIME_ROTATE['level']))
        trh.setFormatter(logging.Formatter(
            settings.TIME_ROTATE['format'], settings.TIME_ROTATE['datefmt']))
        logging.root.addHandler(trh)

        logging.debug('ajilog initialized')
