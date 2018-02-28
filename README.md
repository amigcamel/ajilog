# AjiLog: A Just Intuitive Python logger

|                    |                             |
|--------------------|-----------------------------|
| Travis             | [![Build Status][t1]][t2]   |
| Supported Versions | ![2.7,3.4,3.5,3.6,pypy3][py]        |
| Latest Version     | [![Latest Version][ver]][link] |
---

[t1]: https://travis-ci.org/amigcamel/ajilog.svg?branch=master
[t2]: mahttps://travis-ci.org/amigcamel/ajilog
[py]: https://img.shields.io/badge/python-2.7%2C3.4%2C3.5%2C3.6%2Cpypy3-green.svg
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

## Custom settings

Add `ajilog.conf` to your project:

    [rotate]
    enable = true
    level  = debug
    dir    = /tmp/ajilog
