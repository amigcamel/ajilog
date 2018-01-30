# AjiLog: A Just Intuitive Python logger

|                    |                             |
|--------------------|-----------------------------|
| Supported Versions | ![2.7, 3.5, 3.6][py]        |
| Latest Version     | [![Latest Version][ver]][link] |
---

[py]: https://img.shields.io/badge/python-2.7%2C3.5%2C3.6-green.svg
[link]: https://pypi.python.org/pypi/ajilog
[ver]: https://img.shields.io/pypi/v/ajilog.svg

**AjiLog** provides a fast and intuitive way to implement Python `logging` in your project.  


## Installation

    pip install ajilog
    
## Usage

    from ajilog import logger
    
    logger.debug('DEBUG')
    logger.info('INFO')
    logger.warning('WARNING')
    logger.error('ERROR')
    logger.critical('CRITICAL')
