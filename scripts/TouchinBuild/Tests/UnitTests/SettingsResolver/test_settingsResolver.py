import unittest
from Core.DependencyResolver.SettingsResolver import SettingsResolver


class TestSettingsResolver(unittest.TestCase):
	def test_resolveSettings(self):
		unresolvedSettings = {
			'key1': 'value1',
			'key2': 'value2',
			'key3': '{@key1} {@key2}',
			'key4': '{@key1} {@key3}',

			'key5': 'value5',
			'key6': '{@key5} value6'
		}

		settingsResolver = SettingsResolver(unresolvedSettings)
		resolvedSettings = settingsResolver.resolveSettings()

		self.assertEqual('value1', resolvedSettings['key1'])
		self.assertEqual('value2', resolvedSettings['key2'])
		self.assertEqual('value1 value2', resolvedSettings['key3'])
		self.assertEqual('value1 value1 value2', resolvedSettings['key4'])

		self.assertEqual('value5', resolvedSettings['key5'])
		self.assertEqual('value5 value6', resolvedSettings['key6'])