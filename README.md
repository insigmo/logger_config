logger-config: Configurable and flexible logger for your python applications
============================================================================

Build Status
------------

|travis status| |coverage| |health|

Project details
---------------

|license| |pypi|

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/insigmo/logger_config/blob/master/LICENSE.txt
   :alt: License
.. |pypi| image:: https://badge.fury.io/py/config-logger.svg
   :target: https://pypi.org/project/logger-config/
   :alt: Pypi Version


Description
-----------

The **logger-config** package is a basic configurable logger. This package is currently tested on Python =< 2.7.

- `Issue tracker`_
- `Changelog`_

Installation
------------

::

    pip install logger-config

or

download the `latest release`_ and run

::

    python setup.py install


Usage
-----

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::
    import logging
    
    from logger_config import configure_logging
    
    logger_name = 'root_logger'
    configure_logging(logger_name, log_dir='logs', log_level=logging.DEBUG)
    logger = logging.getLogger(logger_name)
    
    
    logger.warning('This is warning')
    logger.error('This is exception')
    logger.info('This is info message')
    logger.debug('This is debug message')

**Console Output**

::

    [2022-01-07 22:41:52,153] [MainThread] [WARNING] This is warning
    [2022-01-07 22:41:52,153] [MainThread] [ERROR] This is exception
    [2022-01-07 22:41:52,153] [MainThread] [INFO] This is info message


License
-------

This project is licensed under the MIT license.

.. _Issue tracker: https://github.com/insigmo/logger_config/issues
.. _latest release: https://github.com/afxentios/config-logger/releases
.. _this repo: https://github.com/insigmo/logger_config