import unittest
from parsers.SettingsParser.SettingsMerger import SettingsMerger


class TestSettingsMerger(unittest.TestCase):
	def setUp(self):
		self.merger = SettingsMerger()
		self.globalSettings = {
			'top_level_key1': 'value1',
			'top_level_key2': 'value2',

			'child1': {
					'sub_key1': 'value3',
					'sub_key2': 'value4',
				},

			'child2': {
					'sub_key3': 'value5',
					'sub_key4': 'value6',
				}
		}

	def test_mergeTopLevelSettings(self):
		description = {
			'segments': ['top_level_key1'],
			'value': 'new_value1'
		}

		self.merger.merge(self.globalSettings, description)

		self.assertEqual('new_value1', self.globalSettings['top_level_key1'])
		self.assertEqual('value2', self.globalSettings['top_level_key2'])

	def test_mergeSubElement(self):
		description = {
			'segments': ['child1', 'sub_key1'],
			'value': 'new_value3'
		}

		self.merger.merge(self.globalSettings, description)

		self.assertEqual('value1', self.globalSettings['top_level_key1'])
		self.assertEqual('value2', self.globalSettings['top_level_key2'])

		self.assertEqual('new_value3', self.globalSettings['child1']['sub_key1'])
		self.assertEqual('value4', self.globalSettings['child1']['sub_key2'])

	def test_getPropertyName(self):
		self.checkName(['one', 'two', 'three'], 'three')
		self.checkName(['one', 'two'], 'two')
		self.checkName(['one'], 'one')

	def checkName(self, segments, expectedName):
		name = self.merger.getPropertyName(segments)
		self.assertEqual(name, expectedName)

	def test_checkPath(self):
		self.checkPath(['one', 'two', 'three'], ['one', 'two'])
		self.checkPath(['one', 'two'], ['one'])
		self.checkPath(['one'], [])

	def checkPath(self, segments, expectedPath):
		path = self.merger.getPath(segments)

		self.assertListEqual(expectedPath, path)

	def test_mergeNotExistSetting(self):
		description = {
			'segments': ['new_key'],
			'value': 'new_value'
		}

		print self.globalSettings
		self.assertEqual('new_value', self.globalSettings['new_key'])


