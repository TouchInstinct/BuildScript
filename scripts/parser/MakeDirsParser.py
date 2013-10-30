from parser.LineParser import LineParser
import re

class MakeDirsParser(LineParser):
	def parseLine(self, line):
		pathRegexp = r"'(?P<path>[^']+)'$"

		regexpSource = self.startsWithKeywordToken('create dirs') + pathRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		path = match.group('path')
		return path

	def isValidLine(self, line):
		assert line is not None

		return line.startswith('create dirs ')
