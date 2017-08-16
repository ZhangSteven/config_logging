# config_logging

Illustrate a common way to use python logging.

To test, run:

	python main.py

To use logging:

1. Copy the logging.config file to the package you are using.
2. Default settings in logging.config:
	a) log to console and file at the same time.
	b) console log level is WARNING and file log level is DEBUG.
	c) log file name is applog.log in local directory, with 5 rotating files, each of size 20KB.

3. Initialize root logger at the main module (see main.py):
	logging.config.fileConfig(logging.config, disable_existing_loggers=False)

4. logging-more.config add another file handler to root logger, so that one log file
	captures all log messages, the other log file captures only errors.