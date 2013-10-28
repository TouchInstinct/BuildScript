import unittest
from parser.BackupParser.DeleteBackupParser import DeleteBackupParser


class TestDeleteBackupParser(unittest.TestCase):
	def setUp(self):
		self.__parser = DeleteBackupParser()

	def test_isValid(self):
		line = 'delete backup'
		isValid = self.__parser.isValidLine(line)

		self.assertEqual(True, isValid)

	def test_isNotValid(self):
		line = 'bla backup'
		isValid = self.__parser.isValidLine(line)

		self.assertEqual(False, isValid)

	def test_validInput(self):
		line = 'delete backup'
		self.__parser.parseLine(line)