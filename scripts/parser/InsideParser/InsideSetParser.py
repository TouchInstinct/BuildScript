from parser.LineParser import LineParser
import re

class InsideSetParser(LineParser):
	def __init__(self, value_provider, fileExt):
		assert value_provider is not None

		self.__value_provider = value_provider
		self.__extension = fileExt

	def parseLine(self, line):
		assert line is not None

		filePathRegexp = r"'(?P<file>[./ a-zA-Z]+\.{0})'".format(self.__extension)
		keyRegexp = r'(?P<key>[a-zA-Z]+)'
		valueRegexp = r"'(?P<value>[^']+)'"

		regexpSource = self.startsWithKeywordToken('inside') + filePathRegexp + self.keywordToken('set') + keyRegexp + self.keywordToken('to') + valueRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		filePath = match.group('file')
		key = match.group('key')
		value = match.group('value')

		return (filePath, key, value)

	def isValidLine(self, line):
		regexpSrc = r"inside\s+'[./ a-zA-Z]+\.{0}'\s+set".format(self.__extension)
		print regexpSrc
		regexp = re.compile(regexpSrc, re.UNICODE)

		match = regexp.match(line)
		return match is not None