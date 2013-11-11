import unittest
from utils.MacroProcessor import MacroProcessor


class TestMacro(unittest.TestCase):
	def setUp(self):
		self.macroParser = MacroProcessor()

	def test_parseMacros(self):
		line = 'hello {@this} is {@my_macro} and {@macro_with_numbers123}'
		symbols = self.macroParser.getSymbols(line)

		self.assertEqual(3, len(symbols))
		self.assertTrue('@this' in symbols)
		self.assertTrue('@my_macro' in symbols)
		self.assertTrue('@macro_with_numbers123' in symbols)

	def test_parseMacroInsideInclude(self):
		line = "<include '{@path_to_file}'>"
		symbols = self.macroParser.getSymbols(line)

		self.assertTrue('@path_to_file' in symbols)

	def test_parseMacroInsideIncludeWithDirSeparator(self):
		line = "<include '{@parent_folder}/{@folder}/{@file_name}'>"
		symbols = self.macroParser.getSymbols(line)

		self.assertTrue('@parent_folder' in symbols)
		self.assertTrue('@folder' in symbols)
		self.assertTrue('@file_name' in symbols)

	def test_getName(self):
		line = '{@macro_name}'
		name = self.macroParser.getMacroName(line)

		self.assertEqual('@macro_name', name)

	def test_getMacro(self):
		line = '@some_name'
		macro = self.macroParser.getMacroByName(line)

		self.assertEqual('{@some_name}', macro)