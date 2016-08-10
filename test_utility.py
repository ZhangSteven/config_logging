# coding=utf-8
# 
# Illustrate how to use the logging and config file utility.
#


import logging
from config_logging.utility import config, logger 	# the log and config object



def foo():
	global config 	# access the config object
	print('config file has sections: {0}'.format(config.sections()))

	x = 5
	y = config['func']['value']	# read a string value from config object
	logger.debug('value = {0}'.format(x * y))

	try:
		bar()
	except:
		# show how log an exception
		logger.exception("something is wrong")



def bar():
	raise ValueError()



if __name__ == '__main__':
	foo()

