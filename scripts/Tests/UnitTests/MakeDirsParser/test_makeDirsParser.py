import unittest
from parser.MakeDirsParser import MakeDirsParser


class TestMakeDirsParser(unittest.TestCase):
	def setUp(self):
		self.parser = MakeDirsParser()

	def test_isValid(self):
		line = 'create dirs bla bla'
		isValid = self.parser.isValidLine(line)

		self.assertEqual(True, isValid)

	def test_isNotValid(self):
		line = 'create 		 dirs bla bla'
		isValid = self.parser.isValidLine(line)

		self.assertEqual(False, isValid)

	def test_parse(self):
		line = r"create dirs '~/Some dir/../'"
		path = self.parser.parseLine(line)

		self.assertEqual('~/Some dir/../', path)
