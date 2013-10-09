import unittest
from parser.ProjectParser.Project import Project
from parser.ProjectParser.ProjectSetting.AttribureSetting import AttributeSetting


class TestCase(unittest.TestCase):
	def setUp(self):
		self.csproj = Project('appName')

	def test_apply(self):
		attr_value = 'parent_dir/child_dir'
		setting = AttributeSetting('rel_path', attr_value)

		setting.apply(self.csproj)
		self.assertEqual(self.csproj.rel_path, attr_value)
