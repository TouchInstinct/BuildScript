import unittest
from parser.SettingsParser.PathParser import PathParser


class TestPathParser(unittest.TestCase):
	def setUp(self):
		self.parser = PathParser()

	def test_parseValidInput(self):
		propertyPath = '123.abc.some_name'
		segments = self.parser.parsePath(propertyPath)

		self.assertEqual(3, len(segments))
		self.assertEqual('123', segments[0])
		self.assertEqual('abc', segments[1])
		self.assertEqual('some_name', segments[2])