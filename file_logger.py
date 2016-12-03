# coding=utf-8
# 
# This file contains sample code for logging and config file. When this
# module is imported, it will initialize logging and read the config file
# and load the config object.
#
# See test_utility.py on how to use it.
# 
import logging



def convert_log_level(log_level):
	"""
	Convert the log level specified in the config file to the numerical
	values required by the logging module.
	"""
	if log_level == 'debug':
		return logging.DEBUG
	elif log_level == 'info':
		return logging.INFO
	elif log_level == 'warning':
		return logging.WARNING
	elif log_level == 'error':
		return logging.ERROR
	elif log_level == 'critical':
		return logging.CRITICAL
	else:
		return logging.DEBUG



def get_file_logger(log_file, log_level, 
			fmt='%(asctime)s - %(module)s - %(levelname)s: %(message)s'):
    """ 
    Original code from:
    https://gimmebar-assets.s3.amazonaws.com/4fe38b76be0a5.html
    """
    # print('log file = {0}'.format(log_file))
    logging.basicConfig(level=convert_log_level(log_level), filename=log_file, 
    					format=fmt)
    return logging.getLogger('root')


# def _create_logger():
#     """ 
#     Creates a logger based on the python logging package. Supposed to be 
#     called only once.

#     Original code from:
#     http://stackoverflow.com/questions/7621897/python-logging-module-globally
#     """

#     # use the config object
#     global config

#     filename = config['logging']['log_file']
#     filename = get_current_path() + '\\' + filename

#     formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
#     handler = logging.FileHandler(filename)
#     handler.setFormatter(formatter)

#     logger_name = config['logging']['logger_name']
#     log_level = config['logging']['log_level']
#     log_level = convert_log_level(log_level)

#     logger = logging.getLogger(logger_name)
#     logger.setLevel(log_level)
#     logger.addHandler(handler)
    
#     return logger