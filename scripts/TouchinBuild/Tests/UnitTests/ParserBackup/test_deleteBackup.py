import unittest
from parsers.ParserBackup.DeleteBackupParser import DeleteBackupParser


class TestDeleteBackup(unittest.TestCase):
	def setUp(self):
		self.parser = DeleteBackupParser()

	def test_parseCurrentDir(self):
		line = "delete  backup '.'"
		folderPath = self.parser.parseLine(line)

		self.assertEqual('.', folderPath)

	def test_parseRelativePath(self):
		line = "delete backup '../Some/Path'"
		folderPath = self.parser.parseLine(line)

		self.assertEqual('../Some/Path', folderPath)

	def test_parseAbsPath(self):
		line = "delete backup '/Some/Abs/Path'"
		folderPath = self.parser.parseLine(line)

		self.assertEqual('/Some/Abs/Path', folderPath)