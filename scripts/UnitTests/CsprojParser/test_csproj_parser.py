import unittest
from parser.CsprojParser import CsprojParser


class TestCsprojParser(unittest.TestCase):

	def setUp(self):
		self.config = {}
		self.parser = CsprojParser(self.config)


	def test_isCsprojStatement(self):
		expect_true = self.parser.isCsprojStatement('csproj')
		expect_false = self.parser.isCsprojStatement('bla bla bla')

		self.assertEqual(expect_true, True)
		self.assertEqual(expect_false, False)



