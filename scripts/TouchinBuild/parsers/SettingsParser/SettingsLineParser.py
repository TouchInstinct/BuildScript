import re

from parsers.LineParser import LineParser
from parsers.SettingsParser.PathParser import PathParser


class SettingsLineParser(LineParser):
	def __init__(self):
		LineParser.__init__(self)

	def parseLine(self, line):
		assert line is not None

		pathAndValue = self.splitToPathAndValue(line)

		path = pathAndValue[0]
		value = pathAndValue[1]

		pathParser = PathParser()
		pathSegments = pathParser.parse(path)

		result = {
			'segments' : pathSegments,
			'value' : value
		}

		return result

	def splitToPathAndValue(self, line):
		# some.path = some_value
		result = line.split('=')

		propPath = self.getPropertyPath(result[0])
		value = self.getValue(result[1])

		return propPath, value

	def getPropertyPath(self, rawPropertyPath):
		assert rawPropertyPath is not None
		stripped = rawPropertyPath.strip()

		propPathRegexp = r"^(?P<prop_path>[\w.]+)$"
		regexp = re.compile(propPathRegexp, re.UNICODE)

		match = regexp.match(stripped)
		self._guardMatch(match, stripped, propPathRegexp)

		propPath = match.group('prop_path')
		return propPath

	def getValue(self, rawValue):
		assert rawValue is not None
		stripped = rawValue.strip()

		old = stripped
		stripped = stripped.strip("'")

		if old == stripped:
			stripped = stripped.strip('"')

		return stripped