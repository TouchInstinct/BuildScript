import re

from parsers.ParserBackup.ParserBackupBase import ParserBackupBase


class DeleteBackupParser(ParserBackupBase):
	def __init__(self):
		ParserBackupBase.__init__(self)

	def getMatchInfo(self, line):
		assert line is not None

		regexpSource = self.startsWith('delete') + self.endsWith('backup')
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		return match, regexpSource