# coding=utf-8
# 
# Illustrate how to use the logging and config file utility.
#


import logging
from config_logging.utility import config 	# the config object



def foo():
	global config 	# access the config object
	print('config file has sections: {0}'.format(config.sections()))

	x = 5
	y = config['func']['value']	# read a string value
	logging.log(logging.DEBUG, 'value = {0}'.format(x * y))

	try:
		bar()
	except:
		# show how log an exception
		logging.exception("something is wrong")



def bar():
	raise ValueError()