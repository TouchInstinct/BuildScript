import unittest
from parser.CopyParser.CopyArguments import CopyArguments


class TestCopyArguments(unittest.TestCase):
	def setUp(self):
		self.__copyArguments = CopyArguments()

	def test_isValid(self):
		self.__copyArguments.setArguments("someVal1", "someVal2")
		isValid = self.__copyArguments.isValid()

		self.assertEqual(True, isValid)

	def test_notValid(self):
		self.__copyArguments.setArguments(None, "someVal2")
		isValid = self.__copyArguments.isValid()

		self.assertEqual(False, isValid)