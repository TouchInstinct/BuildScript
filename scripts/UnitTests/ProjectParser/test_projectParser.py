# -*- coding: utf-8 -*-
import unittest
from UnitTests.ProjectParser.ValueProvider import ValueProvider
from parser.InsideParser.InsideParser import InsideParser


class TestCsprojParser(unittest.TestCase):

	def setUp(self):
		value_provider = ValueProvider()
		self.parser = InsideParser(value_provider, 'csproj')


	def test_isValid(self):
		line = "inside 'CoolApp.csproj' set KEY to 'VALUE'"
		isValid = self.parser.isValidLine(line)

		self.assertEqual(True, isValid)

	def test_isNotValid(self):
		line = "inside 'CoolApp.txt' set KEY to 'VALUE'"
		isValid = self.parser.isValidLine(line)

		self.assertEqual(False, isValid)

	def test_parse(self):
		line = "inside 'Dir/../Some Folder/CoolApp.csproj' set OutputPath to 'Output'"
		tuple = self.parser.parseLine(line)

		self.assertEqual('Dir/../Some Folder/CoolApp.csproj', tuple[0])
		self.assertEqual('OutputPath', tuple[1])
		self.assertEqual('Output', tuple[2])