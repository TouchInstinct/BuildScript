import unittest
from parsers.InsideParser.InsideRemoveParser import InsideRemoveParser


class TestInsideRemoveParser(unittest.TestCase):
	def setUp(self):
		self.parser = InsideRemoveParser('ext')

	def test_parse(self):
		self.check("inside 'Some/Path/file.ext' remove 'PROGECT' project", 'Some/Path/file.ext', ['PROGECT'])

		self.check("inside 'file.ext' remove 'PR' projects", 'file.ext', ['PR'])
		self.check("inside  'file.ext'  remove  'PR'  projects", 'file.ext', ['PR'])

		self.check("inside 'file.ext' remove 'pr1:pr2:pr3' projects", 'file.ext', ['pr1', 'pr2', 'pr3'])

	def check(self, line, filePath, expectedNames):
		result = self.parser.parseLine(line)

		self.assertEqual(filePath, result['file_path'])
		self.assertListEqual(expectedNames, result['names'])
