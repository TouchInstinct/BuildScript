import re
from parsers.InsideParser.InsideParserBase import InsideParserBase
from parsers.RegexpBuilder import RegexpBuilder


class InsideSetParser(InsideParserBase):
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

		keyRegexp = r'(?P<key>\S+)'
		valueRegexp = r"'(?P<value>[^']+)'$"

		rb = RegexpBuilder()
		regexpSource = rb.startsWith('inside') + self.filePathRegexp + rb.keywordToken('set') + keyRegexp + \
					   rb.keywordToken('to') + valueRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)

		return match, regexpSource