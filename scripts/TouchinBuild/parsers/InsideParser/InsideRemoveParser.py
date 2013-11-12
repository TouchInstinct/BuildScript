import re
from parsers.InsideParser.InsideParserBase import InsideParserBase


class InsideRemoveParser(InsideParserBase):
	def __init__(self, fileExt):
		InsideParserBase.__init__(self, fileExt)

	def parseLine(self, line):
		match = self.fetchMatchFor(line)

		filePath = match.group('file')
		projectName = match.group('project')

		return filePath, projectName

	def getMatchInfo(self, line):
		assert line is not None

		filePathRegexp = r"'(?P<file>[./ a-zA-Z]+\.{0})'".format(self.fileExt)
		projectNameRegexp = r'(?P<project>[.a-zA-Z]+)'

		regexpSource = self.startsWith('inside') + filePathRegexp + self.keywordToken('remove') + projectNameRegexp + self.spaceEndsWith('project')
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		return match, regexpSource