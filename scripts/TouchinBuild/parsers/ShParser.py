import re

from parsers.LineParser import LineParser
from parsers.RegexpBuilder import RegexpBuilder


class ShParser(LineParser):
	def __init__(self):
		LineParser.__init__(self)

	def parseLine(self, line):
		assert line

		rb = RegexpBuilder()
		cmdTextRegexp = r'(?P<text>.*)'

		regexpSource = rb.startsWith('sh') + cmdTextRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		cmdText = match.group('text')
		return cmdText

	def isValidLine(self, line):
		assert line is not None

		return line.startswith('sh ')
