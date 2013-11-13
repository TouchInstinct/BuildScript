import unittest
from Core.LineConveyor.TextInclude import TextInclude
from utils.IncludeProcessor import IncludeProcessor


#noinspection PyUnusedLocal
class MockContentProvider:
	def __init__(self):
		pass

	def fetchContent(self, path):
		return """line 1
line 2
line 3"""

class TestIncludeText(unittest.TestCase):
	def setUp(self):
		includeProcessor = IncludeProcessor()
		contentProvider = MockContentProvider()
		self.includeText = TextInclude(includeProcessor, contentProvider)

	def test_includeText(self):
		text = """
bla bla
<include 'path1'>
another bla
<include 'paht2'>
yet another bla"""

		processedText = self.includeText.processText(text, self.includeText)

		expected = """
bla bla
line 1
line 2
line 3
another bla
line 1
line 2
line 3
yet another bla"""

		self.assertEqual(expected, processedText)
