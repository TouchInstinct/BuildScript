# -*- coding: utf-8 -*-
import unittest
from parsers.SettingsParser.SettingsLineParser import SettingsLineParser


class TestSettingsLineParser(unittest.TestCase):
	def setUp(self):
		self.parser = SettingsLineParser()

	def test_getPathAndValue(self):
		line = "abc.123.some_name = 'crazy value ±~ ../ 123'"
		result = self.parser.splitToPathAndValue(line)

		self.assertEqual('abc.123.some_name', result[0])
		self.assertEqual('crazy value ±~ ../ 123', result[1])
