import re
from parsers.InsideParser.InsideParserBase import InsideParserBase
from parsers.RegexpBuilder import RegexpBuilder


class InsideCsprojSetParser(InsideParserBase):
	def __init__(self, fileExt):
		InsideParserBase.__init__(self, fileExt)

	def parseLine(self, line):
		match = self.fetchMatchFor(line)

		filePath = match.group('file')
		key = match.group('key')
		value = match.group('value')
		slnConfig = match.group('config')

		return filePath, key, value, slnConfig

	def getMatchInfo(self, line):
		assert line is not None

		keyRegexp = r'(?P<key>[a-zA-Z]+)'
		valueRegexp = r"'(?P<value>[^']+)'"
		slnConfigRegexp = r"'(?P<config>[a-zA-Z|]*)'$"

		rb = RegexpBuilder()
		regexpSource = rb.startsWith('inside') + self.filePathRegexp + rb.keywordToken('set') + keyRegexp + \
					   rb.keywordToken('to') + valueRegexp + rb.keywordToken('for') + slnConfigRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		return match, regexpSource