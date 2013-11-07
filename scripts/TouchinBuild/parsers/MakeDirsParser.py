import re

from parsers.LineParser import LineParser


class MakeDirsParser(LineParser):
	def __init__(self):
		LineParser.__init__(self)

	def parseLine(self, line):
		pathRegexp = r"'(?P<path>[^']+)'$"

		regexpSource = self.startsWith('create dirs') + pathRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		path = match.group('path')
		return path

	def isValidLine(self, line):
		assert line is not None

		return line.startswith('create dirs ')
