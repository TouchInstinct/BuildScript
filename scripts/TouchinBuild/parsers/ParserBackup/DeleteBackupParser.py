import re

from parsers.ParserBackup.ParserBackupBase import ParserBackupBase
from parsers.RegexpBuilder import RegexpBuilder


class DeleteBackupParser(ParserBackupBase):
	def __init__(self):
		ParserBackupBase.__init__(self)

	def getMatchInfo(self, line):
		assert line is not None

		rb = RegexpBuilder()
		regexpSource = rb.startsWith('delete') + rb.endsWith('backup')
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		return match, regexpSource