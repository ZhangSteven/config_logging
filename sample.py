# coding=utf-8
# 
import logging

# If you do logger setup at module level, when the module is imported by
# other modules, then you need to make sure root logger is setup
# before this module is imported, it can be tricky.
# 
# Therefore, instead of doing it at the module level, we do it inside
# the functions.
# 
logger = logging.getLogger(__name__)
logger.info('module {0} imported.'.format(__name__))


def do_work():
	for i in range(5):
		logger.debug('do_work(): debug message: {0}'.format(i))
		logger.info('do_work(): info message {0}'.format(i))
		logger.warning('do_work(): warning message {0}'.format(i))
		logger.error('do_work(): error message {0}'.format(i))
		logger.critical('do_work(): critical message {0}'.format(i))