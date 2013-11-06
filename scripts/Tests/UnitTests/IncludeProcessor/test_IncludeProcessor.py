import unittest
from utils.IncludeProcessor import IncludeProcessor


class TestIncludeProcessor(unittest.TestCase):
	def setUp(self):
		self.processor = IncludeProcessor()

	def test_getPathByIncludeStatement(self):
		statement = "< include   'Some Path'>"
		path = self.processor.getPathByIncludeStatement(statement)

		self.assertEqual('Some Path', path)

	def test_getInfos(self):
		text = """
< include 'path1'>
bla bla
<include 'path2'>
some text
"""
		includeInfo = self.processor.getIncludesInfo(text)

		self.assertEqual(2, len(includeInfo))

		info0 = includeInfo[0]
		self.assertEqual("< include 'path1'>", info0[0])
		self.assertEqual('path1', info0[1])

		info1 = includeInfo[1]
		self.assertEqual("<include 'path2'>", info1[0])
		self.assertEqual('path2', info1[1])