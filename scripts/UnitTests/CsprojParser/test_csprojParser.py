import unittest
from parser.CsprojParser.CsprojParser import CsprojParser


class TestCase(unittest.TestCase):
	def setUp(self):
		self.__lineCollection = [
			"csproj app:first key:key1 'value1'",
			"csproj app:first key:key2 'value2'",
			"csproj app:first attr1 'attr_val1'",
			"csproj app:first attr2 'attr_val2'",

			"csproj app:second key:key1 'value1'",
			"csproj app:second key:key2 'value2'",
			"csproj app:second attr1 'attr_val1'",
			"csproj app:second attr2 'attr_val2'"]
		self.__parser = None

	def __do_parse(self):
		self.__parser = CsprojParser(self.__lineCollection)
		self.__parser.parse()

	def test_projectCount(self):
		self.__do_parse()

		self.assertEqual(2, len(self.__parser.projects_dict))
		self.assertTrue('first' in self.__parser.projects_dict)
		self.assertTrue('second' in self.__parser.projects_dict)

	def test_projectSettings(self):
		self.__do_parse()

		first = self.__parser.projects_dict['first']
		second = self.__parser.projects_dict['second']

		self.assertEqual(first.appName, 'first')
		self.assertEqual(second.appName, 'second')

		setting_dict = {
			'key1': 'value1',
			'key2': 'value2'
		}
		self.assertDictEqual(first.settings, setting_dict)
		self.assertDictEqual(second.settings, setting_dict)

		self.assertEqual(first.attr1, 'attr_val1')
		self.assertEqual(first.attr2, 'attr_val2')

		self.assertEqual(second.attr1, 'attr_val1')
		self.assertEqual(second.attr2, 'attr_val2')