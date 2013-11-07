# -*- coding: utf-8 -*-
import unittest
from parsers.ShParser import ShParser


class TestShParser(unittest.TestCase):
	def setUp(self):
		self.parser = ShParser()

	def test_isValid(self):
		line = 'sh 123 ./±~ bla'
		isValid = self.parser.isValidLine(line)

		self.assertEqual(True, isValid)

	def test_isNotValid(self):
		line = 'copy 123 ./±~ bla'
		isValid = self.parser.isValidLine(line)

		self.assertEqual(False, isValid)

	def test_Parse(self):
		line = 'sh 123 ./±~ bla'
		shCmdText = self.parser.parseLine(line)

		self.assertEqual('123 ./±~ bla', shCmdText)

