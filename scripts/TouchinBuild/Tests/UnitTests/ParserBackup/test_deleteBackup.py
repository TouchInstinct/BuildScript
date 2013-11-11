import unittest
from parsers.ParserBackup.DeleteBackupParser import DeleteBackupParser


class TestDeleteBackup(unittest.TestCase):
	def setUp(self):
		self.parser = DeleteBackupParser()

	def test_parseCurrentDir(self):
		line = "delete  backup '.'"
		backupArg = self.parser.parseLine(line)

		self.assertEqual('.', backupArg.folderPath)

	def test_parseRelativePath(self):
		line = "delete backup '../Some/Path'"
		backupArg = self.parser.parseLine(line)

		self.assertEqual('../Some/Path', backupArg.folderPath)

	def test_parseAbsPath(self):
		line = "delete backup '/Some/Abs/Path'"
		backupArg = self.parser.parseLine(line)

		self.assertEqual('/Some/Abs/Path', backupArg.folderPath)