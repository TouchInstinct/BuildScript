import unittest
from parser.ProjectParser.Project import Project
from parser.ProjectParser.ProjectSetting.KeyValueSetting import KeyValueSetting


class TestCase(unittest.TestCase):
	def setUp(self):
		self.csproj = Project('appName')

	def test_apply(self):

		key = 'some_key'
		value = 'somve_value'
		setting = KeyValueSetting(key, value)

		self.assertDictEqual(self.csproj.settings, {})

		setting.apply(self.csproj)
		self.assertDictEqual(self.csproj.settings, {key: value})
