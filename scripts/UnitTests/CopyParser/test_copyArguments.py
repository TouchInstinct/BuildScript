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

	def test_safeValues(self):
		self.__copyArguments.setArguments('val1', 'val2')

		safeSrc = self.__copyArguments.getSafeSource()
		safeDst = self.__copyArguments.getSaveTarget()

		self.assertEqual('val1', safeSrc)
		self.assertEqual('val2', safeDst)

	def test_unsafeValues(self):
		self.__copyArguments.setArguments('val1 with ws', 'val2 with ws')

		safeSrc = self.__copyArguments.getSafeSource()
		safeDst = self.__copyArguments.getSaveTarget()

		self.assertEqual('"val1 with ws"', safeSrc)
		self.assertEqual('"val2 with ws"', safeDst)
