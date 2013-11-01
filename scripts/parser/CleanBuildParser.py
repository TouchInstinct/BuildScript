import re

from parser.LineParser import LineParser


class CleanBuildParser(LineParser):
	def __init__(self, commandToken):
		assert commandToken is not None

		self.__commandToken = commandToken

	def parseLine(self, line):
		assert line is not None

		filePathRegexp = r"'(?P<path>[./ a-zA-Z]+\.sln)'"
		slnConfigRegexp = r"'(?P<config>[a-zA-Z|]+)'$"

		regexpSource = self.startsWithKeywordToken(self.__commandToken) + filePathRegexp + self.keywordToken('for') + slnConfigRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		path = match.group('path')
		slnConfig = match.group('config')

		return (path, slnConfig)

	def isValidLine(self, line):
		assert line is not None

		isValid = line.startswith(self.__commandToken)
		return isValid
