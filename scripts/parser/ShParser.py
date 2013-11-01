import re

from parser.LineParser import LineParser


class ShParser(LineParser):
	def parseLine(self, line):
		assert line

		cmdTextRegexp = r'(?P<text>.*)'

		regexpSource = self.startsWithKeywordToken('sh') + cmdTextRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		cmdText = match.group('text')
		return cmdText

	def isValidLine(self, line):
		assert line is not None

		return line.startswith('sh ')