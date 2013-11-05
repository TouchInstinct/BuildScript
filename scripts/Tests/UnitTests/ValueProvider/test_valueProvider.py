import unittest
from commands.ValueProvider import ValueProvider


class TestCase(unittest.TestCase):
	def setUp(self):
		self.__config = {
			'key1': 'value1',
			'key2': 'value2'
		}
		self.__provider = ValueProvider()
		self.__provider.setConfig(self.__config)

	def test_provideByLink(self):
		value1 = self.__provider.getValueFor('@key1')
		value2 = self.__provider.getValueFor('@key2')

		self.assertEqual(value1, 'value1')
		self.assertEqual(value2, 'value2')
