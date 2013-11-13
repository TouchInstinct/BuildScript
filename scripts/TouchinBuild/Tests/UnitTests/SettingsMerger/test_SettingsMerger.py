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

		settingDescr2 = {
			'segments': ['child1', 'sub_key1'],
			'value': 'new_value3'
		}

	def test_mergeTopLevelSettings(self):
		description = {
			'segments': ['top_level_key1'],
			'value': 'new_value1'
		}

		self.merger.merge(self.globalSettings, description)

		self.assertEqual('new_value1', self.globalSettings['top_level_key1'])
		self.assertEqual('value2', self.globalSettings['top_level_key2'])