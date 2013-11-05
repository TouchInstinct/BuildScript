import unittest
from utils.Macro import Macro


class TestMacro(unittest.TestCase):
	def setUp(self):
		self.macroParser = Macro({})

	def test_parseMacros(self):
		line = 'hello {@this} is {@my_macro} and {@macro_with_numbers123}'
		symbols = self.macroParser.getSymbols(line)

		self.assertEqual(3, len(symbols))
		self.assertTrue('this' in symbols)
		self.assertTrue('my_macro' in symbols)
		self.assertTrue('macro_with_numbers123' in symbols)

