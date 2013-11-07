import unittest
from parsers.CleanBuildParser import CleanBuildParser


class TestCleanBuildParser(unittest.TestCase):
	def setUp(self):
		self.parser = CleanBuildParser('CMD_TOKEN')

	def test_isValid(self):
		line = "CMD_TOKEN bla bla"
		isValid = self.parser.isValidLine(line)

		self.assertEqual(True, isValid)

	def test_isNotValid(self):
		line = 'bla bla CMD_TOKEN'
		isValid = self.parser.isValidLine(line)

		self.assertEqual(False, isValid)

	def test_parse(self):
		line = "CMD_TOKEN '../Base dir/Solution.sln' for 'Release|iPhone'"
		result = self.parser.parseLine(line)

		self.assertEqual('../Base dir/Solution.sln', result[0])
		self.assertEqual('Release|iPhone', result[1])