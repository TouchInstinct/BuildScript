import unittest
from parsers.ParserBackup.RestoreBackupParser import RestoreBackupParser


class TestRestoreBackup(unittest.TestCase):
	def setUp(self):
		self.parser = RestoreBackupParser()

	def test_parseCurrentDir(self):
		line = "restore   from  backup '.'"
		backupArg = self.parser.parseLine(line)

		self.assertEqual('.', backupArg.folderPath)

	def test_parseRelativePath(self):
		line = "restore from backup '../Some/Path'"
		backupArg = self.parser.parseLine(line)

		self.assertEqual('../Some/Path', backupArg.folderPath)

	def test_parseAbsPath(self):
		line = "restore from backup '/Some/Abs/Path'"
		backupArg = self.parser.parseLine(line)

		self.assertEqual('/Some/Abs/Path', backupArg.folderPath)