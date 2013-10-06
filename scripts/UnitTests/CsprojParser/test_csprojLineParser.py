# -*- coding: utf-8 -*-
import unittest
from parser.CsprojParser.CsprojLineParser import CsprojLineParser


class TestCsprojParser(unittest.TestCase):

	def setUp(self):
		self.parser = CsprojLineParser()

	def test_parseAppStatement(self):
		statement = "app:SomeAppName"
		app_name = self.parser._CsprojLineParser__parseAppStatement(statement)

		self.assertEqual(app_name, 'SomeAppName')

	def test_parseKeyValueStatement(self):
		statement = r"key:myKey 'my value -bla bla'"
		setting = self.parser._CsprojLineParser__parseKeyValueStatement(statement)

		self.assertEqual(setting.key, 'myKey')
		self.assertEqual(setting.value, 'my value -bla bla')

	def test_parseAttributeStatement(self):
		statement = r"rel_path '../some_dir/some_file.txt'"
		setting = self.parser._CsprojLineParser__parseAttributeStatement(statement)

		self.assertEqual(setting.attribute_name, 'rel_path')
		self.assertEqual(setting.attribute_value, r'../some_dir/some_file.txt')

	def test_parse_keyedCsprojLine(self):
		statement = r"csproj app:coolApp key:CodesignKey 'iPhone Developer: Рустам Заитов (CTL85FZX6K)'"
		setting = self.parser.parse(statement)

		self.assertEqual(setting.appName, 'coolApp')
		self.assertEqual(setting.key, 'CodesignKey')
		self.assertEqual(setting.value, 'iPhone Developer: Рустам Заитов (CTL85FZX6K)')

	def test_parse_attributedCsprojLine(self):
		statement = r"csproj app:coolApp rel_path '../parent_dir/some_file.extension'"
		setting = self.parser.parse(statement)

		self.assertEqual(setting.appName, 'coolApp')
		self.assertEqual(setting.attribute_name, 'rel_path')
		self.assertEqual(setting.attribute_value, '../parent_dir/some_file.extension')