from parser.LineParser import LineParser
import re

class SettingsLineParser(LineParser):
	def parseLine(self, line):
		assert line is not None

		pathAndValue = self.splitToPathAndValue(line)
		propertyPath = pathAndValue[0]
		value = [1]


	def splitToPathAndValue(self, line):

		propPathRegexp = r"^(?P<prop_path>[\w.]+)"
		valueRegexp = "'(?P<value>.*)'"

		regexpSource = propPathRegexp + self.keywordToken('=') + valueRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		propPath = match.group('prop_path')
		value = match.group('value')

		return (propPath, value)