import re
from parsers.LineParser import LineParser


class InstallProfileParser(LineParser):
	def __init__(self):
		LineParser.__init__(self)

	def parseLine(self, line):
		assert line is not None

		profilePathRegexp = r"'(?P<path>[^']+)'$"
		regexpSource = self.startsWith('install') + self.than('profile') + profilePathRegexp

		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		srcPath = match.group('path')
		return srcPath