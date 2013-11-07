import unittest
from Core.LineConveyor.Stripper import Stripper


class TestStripper(unittest.TestCase):
	def setUp(self):
		self.stripper = Stripper()

	def test_stripLine(self):
		line = '  \tSome text \t\r\n'
		newLine = self.stripper.processText(line)

		self.assertEqual('Some text', newLine)