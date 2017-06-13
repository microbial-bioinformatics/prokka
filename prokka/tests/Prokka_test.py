import unittest
import os
import shutil
from prokka.Prokka import Prokka

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','prokka')

class Options:
	def __init__(self, verbose, threads, input_files):	
		self.verbose                    = verbose
		self.threads                    = threads
		self.input_files                = input_files

class TestProkka(unittest.TestCase):
	
	'''Do a full run with multiple FASTA files'''
	def test_fasta_files(self):
			
		options = Options(False, 1,  [os.path.join(data_dir,'sample1.fa')])
		p = Prokka(options)
		self.assertTrue(p.run())
		