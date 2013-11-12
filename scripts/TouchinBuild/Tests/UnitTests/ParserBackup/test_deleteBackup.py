from Tests.UnitTests.LineParserTestCaseBase import LineParserTestCaseBase
from parsers.ParserBackup.DeleteBackupParser import DeleteBackupParser


class TestDeleteBackup(LineParserTestCaseBase):
	def setUp(self):
		self.textParser = DeleteBackupParser()

	def test_isValid(self):
		self.isValidText('delete backup')
		self.isValidText('delete   backup')

	def test_isNotValid(self):
		self.isNotValidText('delete backup   ')
		self.isNotValidText('delete backup bla bla')
