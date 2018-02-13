# AjiLog: A Just Intuitive Python logger

|                    |                                 |
|--------------------|---------------------------------|
| Travis             | [![Build Status][t1]][t2]       |
| Supported Versions | ![2.7,3.4,3.5,3.6,pypy3][py]    |
| Latest Version     | [![Latest Version][ver]][link]  |
| Test Coverage      | [![Coverage Status][co1]][co2]  |
---


[t1]: https://travis-ci.org/amigcamel/ajilog.svg?branch=master
[t2]: mahttps://travis-ci.org/amigcamel/ajilog
[py]: https://img.shields.io/badge/python-2.7%2C3.4%2C3.5%2C3.6%2Cpypy3-green.svg
[link]: https://pypi.python.org/pypi/ajilog
[ver]: https://img.shields.io/pypi/v/ajilog.svg
[co1]: https://coveralls.io/repos/github/amigcamel/ajilog/badge.svg?branch=master
[co2]: https://coveralls.io/github/amigcamel/ajilog?branch=master

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
