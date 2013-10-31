import unittest
from parser.SettingsParser.SettingsParser import SettingsParser



class TestSettingsParser(unittest.TestCase):
	def setUp(self):
		self.parser = SettingsParser()

	def test_getSettingsDictByPath(self):

		len0 = len(self.parser.settings)
		self.assertEqual(0, len0)

		self.parser.getSettingsDictByPath(['one'])
		len1 = len(self.parser.settings)
		self.assertEqual(1, len1)

		self.parser.getSettingsDictByPath(['one', 'two'])
		len1 = len(self.parser.settings)
		self.assertEqual(1, len1)

		self.parser.getSettingsDictByPath(['another', 'two'])
		len2 = len(self.parser.settings)
		self.assertEqual(2, len2)