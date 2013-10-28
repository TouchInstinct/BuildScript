from parser.LineParser import LineParser
import re

class DeleteBackupParser(LineParser):
	def parseLine(self, line):
		assert line is not None

		regexpSource = r'delete backup\s*'
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

	def isValidLine(self, line):
		assert line is not None

		isValid = line.startswith('delete backup')
		return isValid
