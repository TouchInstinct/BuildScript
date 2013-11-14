import re
from parsers.InsideParser.InsideParserBase import InsideParserBase
from parsers.RegexpBuilder import RegexpBuilder
from parsers.ValuesStriper import ValuesStripper


class InsideRemoveParser(InsideParserBase):
	def __init__(self, fileExt):
		InsideParserBase.__init__(self, fileExt)

	def parseLine(self, line):
		match = self.fetchMatchFor(line)

		filePath = match.group('file')
		projectNames = match.group('projects')

		names = self.parseNames(projectNames)
		result = {
			'file_path': filePath,
			'names': names
		}

		return result

	def getMatchInfo(self, line):
		assert line is not None

		filePathRegexp = r"'(?P<file>[./ a-zA-Z]+\.{0})'".format(self.fileExt)
		projectNameRegexp = r"'(?P<projects>[^']+)'"

		rb = RegexpBuilder()
		regexpSource = rb.startsWith('inside') + filePathRegexp + rb.keywordToken('remove') + projectNameRegexp + \
					   rb.spaceEndsWith('project(s)?')
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		return match, regexpSource

	def parseNames(self, namesStr):

		vs = ValuesStripper()
		names = vs.strip(namesStr)

		return names