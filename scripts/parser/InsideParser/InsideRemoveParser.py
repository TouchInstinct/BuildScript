from parser.LineParser import LineParser
import re


class InsideRemoveParser(LineParser):
	def __init__(self, fileExt):
		assert fileExt is not None

		self.__extension = fileExt

	def parseLine(self, line):
		assert line is not None

		filePathRegexp = r"'(?P<file>[./ a-zA-Z]+\.{0})'".format(self.__extension)
		projectNameRegexp = r'(?P<project>[.a-zA-Z]+)'

		regexpSource = self.startsWithKeywordToken('inside') + filePathRegexp + self.keywordToken('remove') + projectNameRegexp + self.endsWithKeywordToken('project')
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		filePath = match.group('file')
		projectName = match.group('project')

		return (filePath, projectName)

	def isValidLine(self, line):
		regexpSrc = r"inside\s+'[./ a-zA-Z]+\.{0}'\s+remove".format(self.__extension)
		print regexpSrc
		regexp = re.compile(regexpSrc, re.UNICODE)

		match = regexp.match(line)
		return match is not None