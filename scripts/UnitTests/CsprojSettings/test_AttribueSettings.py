import unittest
from parser.CsprojParser.Csproj import Csproj
from parser.CsprojParser.CsprojSetting.AttribureSetting import AttributeSetting


class TestCase(unittest.TestCase):
	def setUp(self):
		self.csproj = Csproj('appName')

	def test_apply(self):
		attr_value = 'parent_dir/child_dir'
		setting = AttributeSetting('rel_path', attr_value)

		setting.apply(self.csproj)
		self.assertEqual(self.csproj.rel_path, attr_value)
