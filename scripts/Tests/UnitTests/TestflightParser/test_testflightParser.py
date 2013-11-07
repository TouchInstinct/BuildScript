import unittest
from parsers.TestflightParser import TestflightParser


class TesttestflightParser(unittest.TestCase):
	def setUp(self):
		self.parser = TestflightParser()

	def test_isValid(self):
		line = 'publish bla bla'
		isValid = self.parser.isValidLine(line)

		self.assertEqual(True, isValid)

	def test_isNotValid(self):
		line = '*publish'
		isValid = self.parser.isValidLine(line)

		self.assertEqual(False, isValid)

	def test_validInput(self):
		line = "publish '~/Dir/another dir/file.ipa' to testflight notes = 'hello world! 123' api_token = 'qwerty123' team_token = 'asdfg123'"
		result = self.parser.parseLine(line)

		self.assertEqual('~/Dir/another dir/file.ipa', result['path'])
		self.assertEqual('hello world! 123', result['notes'])
		self.assertEqual('qwerty123',result['api_token'])
		self.assertEqual('asdfg123', result['team_token'])
