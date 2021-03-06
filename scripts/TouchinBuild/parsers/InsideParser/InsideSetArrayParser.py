import re
from parsers.InsideParser.InsideParserBase import InsideParserBase
from parsers.RegexpBuilder import RegexpBuilder
from parsers.ValuesStriper import ValuesStripper


class InsideSetArrayParser(InsideParserBase):
	def __init__(self, fileExt):
		InsideParserBase.__init__(self, fileExt)

		self.values = None

	def parseLine(self, line):
		match = self.fetchMatchFor(line)

		filePath = match.group('file')
		key = match.group('key')
		valuesStr = match.group('values')

		self.values = self.parseValues(valuesStr)

		return filePath, key, valuesStr

	def getMatchInfo(self, line):
		assert line is not None

		keyRegexp = r'(?P<key>[a-zA-Z]+)'
		valueRegexp = r"'(?P<values>[^']+)'$"

		rb = RegexpBuilder()
		regexpSource = rb.startsWith('inside') + self.filePathRegexp + rb.keywordToken('set') + keyRegexp + \
					   rb.keywordToken('with') + rb.than('values') + valueRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)

		return match, regexpSource

	def parseValues(self, valuesStr):
		assert valuesStr is not None
		assert len(valuesStr) > 0

		vs = ValuesStripper()
		values = vs.strip(valuesStr)

		return values