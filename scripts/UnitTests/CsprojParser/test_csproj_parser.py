import unittest
from parser.CsprojParser import CsprojParser
from parser.token import Token


class TestCsprojParser(unittest.TestCase):

	def setUp(self):
		self.config = {'link': 'qwerty'}
		self.parser = CsprojParser(self.config)


	def test_isCsprojStatement(self):
		expect_true = self.parser.isCsprojStatement('csproj')
		expect_false = self.parser.isCsprojStatement('bla bla bla')

		self.assertEqual(expect_true, True)
		self.assertEqual(expect_false, False)

	def test_isAppToken(self):
		expect_true = self.parser.isAppStatement('app:TheCoolApp')
		expect_false = self.parser.isAppStatement('not_app:SomeIdentifier')

		self.assertEqual(expect_true, True)
		self.assertEqual(expect_false, False)

	def test_isKeyToken(self):
		expect_true = self.parser.isKeyStatement('key:MyKey')
		expect_false = self.parser.isKeyStatement('not_key:SomeIdentifier')

		self.assertEqual(expect_true, True)
		self.assertEqual(expect_false, False)

	def test_isAttributeToken(self):
		expect_true = self.parser.isAttributeToken('my_attrib_name')
		expect_false = self.parser.isKeyStatement('not_attrib:SomeIdentifier')

		self.assertEqual(expect_true, True)
		self.assertEqual(expect_false, False)

	def test_parseAppToken(self):
		token = self.parser.parseAppToken('app:MyCoolApp')
		self.assertEqual(token.content, 'MyCoolApp')

	def test_parseKeyToken(self):
		token = self.parser.parseKeyToken('key:someValue')
		self.assertEqual(token.content, 'someValue')

	def test_fetchValueFromValueToken(self):
		token = Token('@link', 'valueToken')
		value = self.parser.fetchValueFromValueToken(token)

		self.assertEqual(value, 'qwerty')

	def test_procCspojStatement(self):
		self.assertEqual(self.parser._token_index, 0)
		self.parser.procCspojStatement('csproj')
		self.assertEqual(self.parser._token_index, 1)



