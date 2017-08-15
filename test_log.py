# coding=utf-8
# 
from config_logging.sample import do_work
import logging



def do_divided_by_zero():
	# it's a good practice to do get logger in each function. 
	logger = logging.getLogger(__name__)
	try:
		1/0.0
	except:
		logger.exception('error(): ')



def do_log():
	logger = logging.getLogger(__name__)
	for i in range(5):
		logger.info('info message {0}'.format(i))
		logger.critical('critical message {0}'.format(i))




if __name__ == '__main__':
	# must setup the root logger at program entry point before
	# any getLogger() calls.
	import logging.config
	logging.config.fileConfig('logging.config')

	do_work()
	do_divided_by_zero()
	do_log()