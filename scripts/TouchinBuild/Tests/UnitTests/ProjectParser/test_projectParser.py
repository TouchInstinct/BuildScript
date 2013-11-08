# -*- coding: utf-8 -*-
import unittest
from parsers.InsideParser.InsideCsprojSetParser import InsideCsprojSetParser


class TestCsprojParser(unittest.TestCase):

	def setUp(self):
		self.parser = InsideCsprojSetParser('csproj')


	def test_isValid(self):
		line = "inside 'CoolApp.csproj' set KEY to 'VALUE' for 'Sln|Config'"
		isValid = self.parser.isValidLine(line)

		self.assertEqual(True, isValid)

	def test_isNotValid(self):
		line = "inside 'CoolApp.txt' set KEY to 'VALUE'"
		isValid = self.parser.isValidLine(line)

		self.assertEqual(False, isValid)

	def test_parse(self):
		line = "inside 'Dir/../Some Folder/CoolApp.csproj' set OutputPath to 'Output' for 'Release|iPhone'"
		result = self.parser.parseLine(line)

		self.assertEqual('Dir/../Some Folder/CoolApp.csproj', result[0])
		self.assertEqual('OutputPath', result[1])
		self.assertEqual('Output', result[2])
		self.assertEqual('Release|iPhone', result[3])