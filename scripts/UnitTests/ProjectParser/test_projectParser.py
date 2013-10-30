# -*- coding: utf-8 -*-
import unittest
from UnitTests.ProjectParser.ValueProvider import ValueProvider
from parser.ProjectParser.ProjectParser import ProjectParser


class TestCsprojParser(unittest.TestCase):

	def setUp(self):
		value_provider = ValueProvider()
		self.parser = ProjectParser(value_provider, 'csproj')


	def test_isValid(self):
		line = "for CoolApp csproj set KEY to 'VALUE'"
		isValid = self.parser.isValidLine(line)

		self.assertEqual(True, isValid)

	def test_isNotValid(self):
		line = "for CoolApp InvalidCmdToken set KEY to 'VALUE'"
		isValid = self.parser.isValidLine(line)

		self.assertEqual(False, isValid)

	def test_parse(self):
		line = "for CoolApp.Touch csproj set OutputPath to 'Output'"
		settings = self.parser.parseLine(line)

		self.assertEqual('CoolApp.Touch', settings.projectName)
		self.assertEqual('OutputPath', settings.key)
		self.assertEqual('Output', settings.value)