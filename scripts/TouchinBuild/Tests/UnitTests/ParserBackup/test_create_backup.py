from Tests.UnitTests.LineParserTestCaseBase import LineParserTestCaseBase
from parsers.ParserBackup.CreateBackupParser import CreateBackupParser


class TestCreateBackup(LineParserTestCaseBase):
	def setUp(self):
		self.textParser = CreateBackupParser()

	def test_isValid(self):
		self.isValidText('create backup')
		self.isValidText('create   backup')

	def test_isNotValid(self):
		self.isNotValidText('create backup  ')
		self.isNotValidText('create backup bla bla')