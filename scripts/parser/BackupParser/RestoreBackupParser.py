import re

from parser.LineParser import LineParser


class RestoreBackupParser(LineParser):
	def __init__(self):
		LineParser.__init__(self)

	def parseLine(self, line):
		assert line is not None

		regexpSource = r'restore from backup\s*'
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

	def isValidLine(self, line):
		assert line is not None

		isValid = line.startswith('restore from backup')
		return isValid

