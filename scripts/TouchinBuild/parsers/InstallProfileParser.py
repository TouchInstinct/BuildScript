import re
from parsers.LineParser import LineParser
from parsers.RegexpBuilder import RegexpBuilder


class InstallProfileParser(LineParser):
	def __init__(self):
		LineParser.__init__(self)

	def parseLine(self, line):
		assert line is not None

		rb = RegexpBuilder()
		profilePathRegexp = r"'(?P<path>[^']+)'$"
		regexpSource = rb.startsWith('install') + rb.than('profile') + profilePathRegexp

		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		srcPath = match.group('path')
		return srcPath

	def isValidLine(self, line):
		rb = RegexpBuilder()

		regexpSource = rb.startsWith('install') + rb.than('profile')
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		return match is not None
