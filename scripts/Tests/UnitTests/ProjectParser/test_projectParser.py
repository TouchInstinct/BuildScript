# -*- coding: utf-8 -*-
import unittest
from commands.ValueProvider import ValueProvider
from parsers.InsideParser.InsideSetParser import InsideSetParser


class TestCsprojParser(unittest.TestCase):

	def setUp(self):
		value_provider = ValueProvider()
		self.parser = InsideSetParser(value_provider, 'csproj')


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
		result = self.parser.parseLine(line)

		self.assertEqual('Dir/../Some Folder/CoolApp.csproj', result[0])
		self.assertEqual('OutputPath', result[1])
		self.assertEqual('Output', result[2])