import sys
import os
import logging
import time

'''
The main driving functionality of the whole application. This takes the input parameters from 
the user and feeds then into different classes to caculate the results.
'''
class Prokka:
	def __init__(self,options):
		self.start_time = int(time.time())
		self.logger = logging.getLogger(__name__)
		self.verbose                    = options.verbose
		self.threads                    = options.threads
		self.input_files                = options.input_files
		
		if self.verbose:
			self.logger.setLevel(logging.DEBUG)
		else:
			self.logger.setLevel(logging.ERROR)

	def run(self):
		self.logger.warning('Starting annotation')

			