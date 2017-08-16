# coding=utf-8
# 
from config_logging.sample import do_work
import logging
logger = logging.getLogger(__name__)



def do_divided_by_zero():
	try:
		1/0.0
	except:
		logger.exception('error(): ')



def do_log():
	for i in range(5):
		logger.info('info message {0}'.format(i))
		logger.critical('critical message {0}'.format(i))



if __name__ == '__main__':
	import logging.config

	# NOTE: disable_existing_loggers must be explicitly set to False, otherwise
	# 	it will disable exising loggers. In our case, all the loggers. Because
	# 	those loggers are created when the modules are imported.
	# 
	# logging.config.fileConfig('logging.config')
	logging.config.fileConfig('logging.config', disable_existing_loggers=False)

	do_work()
	do_divided_by_zero()
	do_log()
