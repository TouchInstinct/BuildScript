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
			'name': None,
			'dict': {
				'key1': 'a',
				'key2': 'b',
				'key3': 'c',
				'key4': 'd'
			}
		}
		wr1 = {
			'parent': wr0,
			'name' : 'name0',
			'dict':{
				'key2': 'bb',
				'key3': 'cc',
				'key4': 'dd',

				'key5': 'ee'
			}
		}
		wr2 = {
		'parent': wr1,
		'name': 'name1',
		'dict':{
			'key3': 'ccc',
			'key4': 'ddd',

			'key6': 'fff'
			}
		}

		configInfo = self.provider.fetchConfigInfoFromLeafWrapper(wr2)
		config = configInfo[1]
		expected = {
			'key1': 'a',
			'key2': 'bb',
			'key3': 'ccc',
			'key4': 'ddd',
			'key5': 'ee',
			'key6': 'fff'
		}
		self.assertDictEqual(expected, config)

	def test_buildReadyNames(self):
		config = {
			'configs': 'ios, android, wp7'
		}

		names = self.provider.fetchBuildReadyConfigNames(config)

		self.assertEqual(3, len(names))
		self.assertTrue('ios' in names)
		self.assertTrue('android' in names)
		self.assertTrue('wp7' in names)

	def test_getConfig(self):
		rootConfig = {
			'configs': 'ios, android',

			'ios': {

			},

			'android': {

			},

			'wp7': {

			}
		}

		configs = self.provider.getConfigs(rootConfig)

		self.assertEqual(2, len(configs))