import re
from parsers.InsideParser.InsideParserBase import InsideParserBase


class InsideSetArrayParser(InsideParserBase):
	def __init__(self, fileExt):
		InsideParserBase.__init__(self, fileExt)

	def parseLine(self, line):
		match = self.fetchMatchFor(line)

		filePath = match.group('file')
		key = match.group('key')
		value = match.group('value')

		return filePath, key, value

	def getMatchInfo(self, line):
		assert line is not None

		keyRegexp = r'(?P<key>[a-zA-Z]+)'
		valueRegexp = r"'(?P<value>[^']+)'$"

		regexpSource = self.startsWith('inside') + self.filePathRegexp + self.keywordToken('set') + keyRegexp + \
					   self.keywordToken('to') + valueRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)

		return match, regexpSource