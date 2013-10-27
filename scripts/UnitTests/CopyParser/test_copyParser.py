import unittest
from parser.CopyParser.CopyLineParser import CopyLineParser


class TestCopyParser(unittest.TestCase):
	def setUp(self):
		self.__parser = CopyLineParser()

	def test_validSrcDst(self):
		cpArgs = self.__parser.parseLine("copy 'File1' to 'File2'")
		self.assertEqual('File1', cpArgs.source)
		self.assertEqual('File2', cpArgs.target)

	def test_withFolder(self):
		cpArgs = self.__parser.parseLine("copy 'dir1/dir2/src.txt' to 'dir3/dir4/dst.txt'")
		self.assertEqual('dir1/dir2/src.txt', cpArgs.source)
		self.assertEqual('dir3/dir4/dst.txt', cpArgs.target)

	def test_withWiteSpace(self):
		cpArgs = self.__parser.parseLine("copy 'dir1 with ws/dir2 with ws/s r c.txt' to 'dir3 with ws/dir4/d s t.txt'")
		self.assertEqual('dir1 with ws/dir2 with ws/s r c.txt', cpArgs.source)
		self.assertEqual('dir3 with ws/dir4/d s t.txt', cpArgs.target)

