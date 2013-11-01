import unittest
from parser.SettingsParser.SettingsParser import SettingsParser



class TestSettingsParser(unittest.TestCase):
	def setUp(self):
		self.parser = SettingsParser()

	def test_processLine(self):
		line1 = "x.y.name1 = 'value1'"
		line2 = "x.y.name2 = 'value2'"
		line3 = "x.z.name1 = 'value3'"
		line4 = "x.z.name2 = 'value4'"

		line5 = "a.y.name1 = 'value5'"
		line6 = "a.y.name2 = 'value6'"
		line7 = "a.z.name1 = 'value7'"
		line8 = "a.z.name2 = 'value8'"

		self.parser.processLine(line1)
		self.parser.processLine(line2)
		self.parser.processLine(line3)
		self.parser.processLine(line4)
		self.parser.processLine(line5)
		self.parser.processLine(line6)
		self.parser.processLine(line7)
		self.parser.processLine(line8)

		self.assertEqual('value1', self.parser.settings['x']['y']['name1'])
		self.assertEqual('value2', self.parser.settings['x']['y']['name2'])
		self.assertEqual('value3', self.parser.settings['x']['z']['name1'])
		self.assertEqual('value4', self.parser.settings['x']['z']['name2'])

		self.assertEqual('value5', self.parser.settings['a']['y']['name1'])
		self.assertEqual('value6', self.parser.settings['a']['y']['name2'])
		self.assertEqual('value7', self.parser.settings['a']['z']['name1'])
		self.assertEqual('value8', self.parser.settings['a']['z']['name2'])

	def test_emptyLinesAndComments(self):
		class PartialSettingsParser(SettingsParser):
			def __init__(self):
				self.processLineCall = 0

			def processLine(self, line):
				self.processLineCall += 1

		self.parser = PartialSettingsParser()
		content = """
valid.line.with.setting = 'some value'
# this is comment

   another.valid.line = 'another value'
		"""

		self.parser.parse(content)

		self.assertEqual(2, self.parser.processLineCall)










