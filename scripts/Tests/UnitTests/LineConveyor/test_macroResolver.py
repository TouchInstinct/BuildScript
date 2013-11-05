import unittest
from Core.LineConveyor.MacroResolver import MacroResolver
from commands.ValueProvider import ValueProvider
from utils.MacroProcessor import MacroProcessor


class TestMacroResolver(unittest.TestCase):
	def setUp(self):
		config = {
			'key1': 'hello world',
			'some_name': 'another name',
			'version': '1.2.3'
		}

		macroProcessor = MacroProcessor()
		valueProvider = ValueProvider(config)
		self.macroResolver = MacroResolver(macroProcessor, valueProvider)

	def test_resolveLine(self):
		line = '{@key1} bla {@some_name} version: {@version}'
		newLine = self.macroResolver.processLine(line)

		self.assertEqual('hello world bla another name version: 1.2.3', newLine)