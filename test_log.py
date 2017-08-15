# coding=utf-8
# 
from config_logging.logging_utility import logger



if __name__ == '__main__':
	try:
		1/0.0
	except:
		logger.exception('error(): ')

	# for i in range(1000):
	# 	logger.debug('debug message: {0}'.format(i))
	# 	logger.info('info message {0}'.format(i))
	# 	logger.warn('warn message {0}'.format(i))
	# 	logger.error('error message {0}'.format(i))
	# 	logger.critical('critical message {0}'.format(i))