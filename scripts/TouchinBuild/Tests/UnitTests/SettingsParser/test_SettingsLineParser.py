# -*- coding: utf-8 -*-
import unittest
from parsers.SettingsParser.SettingsLineParser import SettingsLineParser


class TestSettingsLineParser(unittest.TestCase):
	def setUp(self):
		self.parser = SettingsLineParser()

	def test_whiteSpaces(self):
		self.checkPathAndValue("abc.123.some_name = 'crazy value ±~ ../ 123'", 'abc.123.some_name', 'crazy value ±~ ../ 123')
		self.checkPathAndValue("a.b.c = 'value'", 'a.b.c', 'value')
		self.checkPathAndValue("a.b.c= 'value'", 'a.b.c', 'value')
		self.checkPathAndValue("a.b.c ='value'", 'a.b.c', 'value')
		self.checkPathAndValue("a.b.c='value'", 'a.b.c', 'value')

	def test_valueWithoutComma(self):
		self.checkPathAndValue("a.b.c = value", 'a.b.c', 'value')
		self.checkPathAndValue("a.b.c = some value", 'a.b.c', 'some value')
		self.checkPathAndValue("a.b.c =   some value  ", 'a.b.c', 'some value')

	def test_valueWithEscapeComma(self):
		self.checkPathAndValue("a.b.c = '\"value\"'  ", 'a.b.c', '"value"')
		self.checkPathAndValue('a.b.c = "\'value\'"  ', 'a.b.c', "'value'")

		self.checkPathAndValue('a.b.c = ""value""  ', 'a.b.c', 'value')
		self.checkPathAndValue("a.b.c = ''value''  ", 'a.b.c', 'value')

	def checkPathAndValue(self, line, expectedPath, expectedValue):
		result = self.parser.splitToPathAndValue(line)

		self.assertEqual(expectedPath, result[0])
		self.assertEqual(expectedValue, result[1])
