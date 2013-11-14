from Tests.UnitTests.LineParserTestCaseBase import LineParserTestCaseBase
from parsers.InsideParser.InsideSetArrayParser import InsideSetArrayParser


class TestInsideSetArrayParser(LineParserTestCaseBase):
	_validSingleValueTest = "inside 'my.txt' set KEY with values 'value1'"
	_validMultiValueTest = "inside 'my.txt' set KEY with values 'value1:value2:value3'"

	def setUp(self):
		self.textParser = InsideSetArrayParser('txt')

	def test_isValid(self):
		self.isValidText(TestInsideSetArrayParser._validSingleValueTest)
		self.isValidText(TestInsideSetArrayParser._validMultiValueTest)
		self.isValidText("inside   'my.txt'   set   KEY   with   values   'value1:value2:value3'")

	def test_isNotValid(self):
		self.isNotValidText("inside 'my.sln' set KEY with values 'value1'")
		self.isNotValidText("inside 'my.sln' set KEY with values 'value1:value2'")
		self.isNotValidText("inside 'my.txt' set KEY with values 'value1'   ")
		self.isNotValidText("inside 'my.txt' set KEY with values 'value1' bla bla")


	def test_parse(self):
		self.checkParse(TestInsideSetArrayParser._validSingleValueTest, 'my.txt', 'KEY', 'value1')
		self.checkParse(TestInsideSetArrayParser._validMultiValueTest, 'my.txt', 'KEY', 'value1:value2:value3')

	def test_values(self):
		self.checkValues(TestInsideSetArrayParser._validSingleValueTest, ['value1'])
		self.checkValues(TestInsideSetArrayParser._validMultiValueTest, ['value1', 'value2', 'value3'])

	def checkParse(self, line, filePath, key, value):
		result = self.textParser.parseLine(line)

		self.assertEqual(filePath, result[0])
		self.assertEqual(key, result[1])
		self.assertEqual(value, result[2])

	def checkValues(self, text, expectedValues):
		self.textParser.parseLine(text)

		self.assertEqual(len(expectedValues), len(self.textParser.values))

		for v in self.textParser.values:
			self.assertTrue(v in expectedValues)