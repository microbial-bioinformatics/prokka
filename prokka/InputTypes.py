import os
import argparse

'''Methods to validate the input parameters passed in by the user'''
class InputTypes:
	
	'''All of the input files listed should exist'''
	def is_fasta_valid(filename):
		if not os.path.exists(filename):
			raise argparse.ArgumentTypeError('Cannot access input file')
		return filename
			
	'''Check the number of threads is sensible'''
	def is_threads_valid(value_str):
		if value_str.isdigit():
			threads = int(value_str)
			if  threads > 0 and threads <= 1024:
				return threads
		raise argparse.ArgumentTypeError("Invalid number of threads, it must at least 1 and less than the No. of CPUs")
		