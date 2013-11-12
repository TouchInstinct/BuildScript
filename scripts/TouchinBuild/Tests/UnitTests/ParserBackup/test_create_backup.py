import unittest
from parsers.ParserBackup.CreateBackupParser import CreateBackupParser


class TestCreateBackup(unittest.TestCase):
	def setUp(self):
		self.parser = CreateBackupParser()

	def test_isValid(self):
		line = "create   backup"
		isValid = self.parser.isValidLine(line)

		self.assertEqual(True, isValid)

	def test_isNotValid(self):
		line = "create backup bla bla"
		isValid = self.parser.isValidLine(line)

		self.assertEqual(False, isValid)