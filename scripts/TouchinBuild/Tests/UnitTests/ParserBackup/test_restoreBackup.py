from Tests.UnitTests.LineParserTestCaseBase import LineParserTestCaseBase
from parsers.ParserBackup.RestoreBackupParser import RestoreBackupParser


class TestRestoreBackup(LineParserTestCaseBase):
	def setUp(self):
		self.textParser = RestoreBackupParser()

	def test_isValid(self):
		self.isValidText('restore from backup')
		self.isValidText('restore   from  backup')

	def test_isNotValid(self):
		self.isNotValidText('restore from backup   ')
		self.isNotValidText('restore from backup bla bla')