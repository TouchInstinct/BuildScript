from unittest.case import TestCase


class LineParserTestCaseBase(TestCase):
	def __init__(self, methodName):
		TestCase.__init__(self, methodName)

		self.textParser = None

	def isValidText(self, text):
		isValid = self.textParser.isValidLine(text)

		self.assertEqual(True, isValid)

	def isNotValidText(self, text):
		isValid = self.textParser.isValidLine(text)

		self.assertEqual(False, isValid)
