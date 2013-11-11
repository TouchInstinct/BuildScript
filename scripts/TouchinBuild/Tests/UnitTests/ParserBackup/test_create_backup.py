import unittest
from parsers.ParserBackup.CreateBackupParser import CreateBackupParser


class TestCreateBackup(unittest.TestCase):
	def setUp(self):
		self.parser = CreateBackupParser()

	def test_parseCurrentDir(self):
		line = "create   backup  for    '.'"
		backupArg = self.parser.parseLine(line)

		self.assertEqual('.', backupArg.folderPath)

	def test_parseRelativePath(self):
		line = "create backup for '../Some/Path'"
		backupArg = self.parser.parseLine(line)

		self.assertEqual('../Some/Path', backupArg.folderPath)

	def test_parseAbsPath(self):
		line = "create backup for '/Some/Abs/Path'"
		backupArg = self.parser.parseLine(line)

		self.assertEqual('/Some/Abs/Path', backupArg.folderPath)