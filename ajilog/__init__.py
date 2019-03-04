from .core import logger

__version_info__ = (0, 0, 4)
__version__ = '.'.join(str(_) for _ in __version_info__)


debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
critical = logger.critical
