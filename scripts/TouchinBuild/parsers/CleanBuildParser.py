import re

from parsers.LineParser import LineParser
from parsers.RegexpBuilder import RegexpBuilder


class CleanBuildParser(LineParser):
	def __init__(self, commandToken):
		LineParser.__init__(self)
		assert commandToken is not None

		self.commandToken = commandToken

	def parseLine(self, line):
		assert line is not None

		filePathRegexp = r"'(?P<path>[./ a-zA-Z]+\.sln)'"
		slnConfigRegexp = r"'(?P<config>[a-zA-Z|]+)'$"

		rb = RegexpBuilder()
		regexpSource = rb.startsWith(self.commandToken) + filePathRegexp + rb.keywordToken('for') + slnConfigRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		path = match.group('path')
		slnConfig = match.group('config')

		return path, slnConfig

	def isValidLine(self, line):
		assert line is not None

		isValid = line.startswith(self.commandToken)
		return isValid
