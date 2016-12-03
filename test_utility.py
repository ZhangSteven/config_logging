# coding=utf-8
# 
# Illustrate how to use the logging and config file utility.
#
from config_logging.utility import logger

import random
import time



if __name__ == '__main__':

	for i in range(5):
		delay = random.randint(0, 5)
		time.sleep(delay/10)
		logger.error('test {0}'.format(i))
