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


def initialize(**kwargs):
    """Call this function to patch the default root logger."""
    # experimental feature: colorize Scrapy log
    if kwargs.get('colorize_scrapy'):
        import scrapy.utils.log
        scrapy.utils.log._get_handler = lambda x: logging.NullHandler()
    # set root logger level to DEBUG
    logging.root.setLevel(logging.DEBUG)
    # stream handler
    if settings.HANDLERS['STREAM']['enabled']:
        StreamHandler(settings.HANDLERS['STREAM'])
    # file handler
    if settings.HANDLERS['FILE']['enabled']:
        FileHandler(settings.HANDLERS['FILE'])
    # rotating file handler
    if settings.HANDLERS['TIME_ROTATE']['enabled']:
        TimedRotatingFileHandler(settings.HANDLERS['TIME_ROTATE'])


class Handler:
    """Logger handler."""

    def __init__(self, params):
        """Build logger."""
        self.params = params
        self.create_handler()
        self.set_formatter()
        self.set_level()
        self.add_handler()
        logging.root.debug('%s added' % self.handler)

    def create_handler(self):
        """Create logger handler."""
        raise NotImplementedError

    def set_level(self):
        """Set log level."""
        self.handler.setLevel(getattr(logging, self.params['level']))

    def set_formatter(self):
        """Set logger format."""
        self.handler.setFormatter(logging.Formatter(
            self.params['format'], self.params['datefmt']))

    def add_handler(self):
        """Add handler to logger."""
        logging.root.addHandler(self.handler)


class StreamHandler(Handler):
    """Build logging.StreamHandler."""

    def create_handler(self):
        """Create logger handler."""
        self.handler = logging.StreamHandler()

    def set_formatter(self):
        """Set logger format."""
        self.handler.setFormatter(ColoredFormatter(
            self.params['format'],
            datefmt=self.params['datefmt'],
            log_colors=self.params['log_colors']))


class FileHandler(Handler):
    """Build logging.FileHandler."""

    def create_handler(self):
        """Create logger handler."""
        self.handler = logging.FileHandler(self.params['path'])


class TimedRotatingFileHandler(Handler):
    """Build logging.handlers.TimedRotatingFileHandler."""

    def create_handler(self):
        """Create handler."""
        self.handler = logging.handlers.TimedRotatingFileHandler(
            self.params['path'],
            when=self.params['when'],
            backupCount=self.params['backupCount'])
