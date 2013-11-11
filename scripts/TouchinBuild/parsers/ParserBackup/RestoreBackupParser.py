import re

from parsers.ParserBackup.ParserBackupBase import ParserBackupBase


class RestoreBackupParser(ParserBackupBase):
	def __init__(self):
		ParserBackupBase.__init__(self)

	def getMatchInfo(self, line):
		assert line is not None

		folderNameRegexp = r"'(?P<folder>[^']+)'$"
		regexpSource = self.startsWith('restore') + self.than('from') + self.than('backup') + folderNameRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		return match, regexpSource