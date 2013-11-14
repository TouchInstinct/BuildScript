import re

from parsers.ParserBackup.ParserBackupBase import ParserBackupBase
from parsers.RegexpBuilder import RegexpBuilder


class RestoreBackupParser(ParserBackupBase):
	def __init__(self):
		ParserBackupBase.__init__(self)

	def getMatchInfo(self, line):
		assert line is not None

		rb = RegexpBuilder()
		regexpSource = rb.startsWith('restore') + rb.than('from') + rb.endsWith('backup')
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		return match, regexpSource