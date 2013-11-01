import unittest
from utils.BuildConfigProvider import BuildConfigProvider


class TestBuildConfigProvider(unittest.TestCase):
	def setUp(self):
		self.provider = BuildConfigProvider()

	def test_getAncestorsFor(self):
		wr0 = {'parent': None}
		wr1 = {'parent': wr0}
		wr2 = {'parent': wr1}

		ancestors = self.provider.getAncestorsFor(wr2)

		self.assertEqual(wr0, ancestors[0])
		self.assertEqual(wr1, ancestors[1])
		self.assertEqual(wr2, ancestors[2])

	def test_unionConfig(self):
		wr0 = {
			'parent': None,
			'dict': {
				'key1': 'a',
				'key2': 'b',
				'key3': 'c',
				'key4': 'd'
			}
		}
		wr1 = {
			'parent': wr0,
			'dict':{
				'key2': 'bb',
				'key3': 'cc',
				'key4': 'dd',

				'key5': 'ee'
			}
		}
		wr2 = {
		'parent': wr1,
		'dict':{
			'key3': 'ccc',
			'key4': 'ddd',

			'key6': 'fff'
			}
		}

		config = self.provider.fetchConfigFromLeafWrapper(wr2)
		expected = {
			'key1': 'a',
			'key2': 'bb',
			'key3': 'ccc',
			'key4': 'ddd',
			'key5': 'ee',
			'key6': 'fff'
		}
		self.assertDictEqual(expected, config)
