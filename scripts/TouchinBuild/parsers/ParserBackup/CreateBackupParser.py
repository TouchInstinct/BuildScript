import re

from parsers.ParserBackup.ParserBackupBase import ParserBackupBase


class CreateBackupParser(ParserBackupBase):
	def __init__(self):
		ParserBackupBase.__init__(self)

	def getMatchInfo(self, line):
		assert line is not None

		folderNameRegexp = r"'(?P<folder>[^']+)'$"

		regexpSource = self.startsWith('create') + self.than('backup') + self.than('for') + folderNameRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		return match, regexpSource