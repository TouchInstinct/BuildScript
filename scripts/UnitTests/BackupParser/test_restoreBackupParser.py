import unittest
from parser.BackupParser.RestoreBackupParser import RestoreBackupParser


class TestRestoreBackupParser(unittest.TestCase):
	def setUp(self):
		self.__parser = RestoreBackupParser()

	def test_ValidInput(self):
		line = 'restore from backup'
		self.__parser.parseLine(line)