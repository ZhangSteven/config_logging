# config_logging

Illustrate a common way to use python logging.

To test, run:

	python test_log.py

To use logging:

1. Copy the logging.config file to the package you are using.
2. Default settings in logging.config:
	a) log to console and file at the same time.
	b) console log level is WARNING and file log level is DEBUG.
	c) log file name is applog.log in local directory, with 5 rotating files, each of size 20KB.

3. Initialize root logger at program entry point, before any getLogger() calls, by (see test_log.py):
	logging.config.fileConfig(logging.config), 