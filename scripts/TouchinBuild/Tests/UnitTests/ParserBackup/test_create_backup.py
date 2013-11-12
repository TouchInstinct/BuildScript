import unittest
from parsers.ParserBackup.CreateBackupParser import CreateBackupParser


class TestCreateBackup(unittest.TestCase):
	def setUp(self):
		self.parser = CreateBackupParser()

	def test_parseCurrentDir(self):
		line = "create   backup  for    '.'"
		folderPath = self.parser.parseLine(line)

		self.assertEqual('.', folderPath)

	def test_parseRelativePath(self):
		line = "create backup for '../Some/Path'"
		folderPath = self.parser.parseLine(line)

		self.assertEqual('../Some/Path', folderPath)

	def test_parseAbsPath(self):
		line = "create backup for '/Some/Abs/Path'"
		folderPath = self.parser.parseLine(line)

		self.assertEqual('/Some/Abs/Path', folderPath)