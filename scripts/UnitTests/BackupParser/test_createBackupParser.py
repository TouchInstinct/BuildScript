import unittest
from parser.BackupParser.CreateBackupParser import CreateBackupParser


class TestCreateBackupParser(unittest.TestCase):
	def setUp(self):
		self.__parser = CreateBackupParser()

	def test_validInput(self):
		line = "create backup for 'SomeFolder'"
		createBackupArgs = self.__parser.parseLine(line)

		self.assertEqual('SomeFolder', createBackupArgs.folderName)