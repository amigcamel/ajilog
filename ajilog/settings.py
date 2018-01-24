"""Logging configurations."""
import logging

from colorlog import ColoredFormatter

loggers = {}


def set_logger(name):
    """Logger."""
    global loggers

    if loggers.get(name):
        return loggers.get(name)
    else:
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

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # StreamHandler
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(formatter)

        # Add handlers
        logger.addHandler(sh)
        loggers[name] = logger
        return logger
