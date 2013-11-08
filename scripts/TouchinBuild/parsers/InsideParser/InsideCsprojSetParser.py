import re

from parsers.LineParser import LineParser


class InsideCsprojSetParser(LineParser):
	def __init__(self, fileExt):
		LineParser.__init__(self)

		self.__extension = fileExt

	def parseLine(self, line):
		assert line is not None

		matchInfo = self.getMatchInfo(line)
		match = matchInfo[0]
		regexpSource = matchInfo[1]
		self._guardMatch(match, line, regexpSource)

		filePath = match.group('file')
		key = match.group('key')
		value = match.group('value')
		slnConfig = match.group('config')

		return filePath, key, value, slnConfig

	def getMatchInfo(self, line):
		assert line is not None

		filePathRegexp = r"'(?P<file>[./ a-zA-Z]+\.{0})'".format(self.__extension)
		keyRegexp = r'(?P<key>[a-zA-Z]+)'
		valueRegexp = r"'(?P<value>[^']+)'"
		slnConfigRegexp = r"'(?P<config>[a-zA-Z|]+)'$"

		regexpSource = self.startsWith('inside') + filePathRegexp + self.keywordToken('set') + keyRegexp + \
					   self.keywordToken('to') + valueRegexp + self.than('for') + slnConfigRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		return match, regexpSource

	def isValidLine(self, line):
		assert line is not None

		matchInfo = self.getMatchInfo(line)
		match = matchInfo[0]

		return match is not None