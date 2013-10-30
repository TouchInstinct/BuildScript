from parser.LineParser import LineParser
from parser.ProjectParser.ProjectSetting.KeyValueSetting import KeyValueSetting
import re

class ProjectParser(LineParser):
	def __init__(self, value_provider, command_token):
		assert value_provider is not None

		self._value_provider = value_provider
		self._command_token = command_token

	def parseLine(self, line):
		assert line is not None

		projectNameRegexp = r"(?P<name>[.a-zA-Z]+)"
		keyRegexp = r'(?P<key>[a-zA-Z]+)'
		valueRegexp = r"'(?P<value>[^']+)'"

		regexpSource = self.startsWithKeywordToken('for') + projectNameRegexp + self.keywordToken(self._command_token + r'\s+set') + keyRegexp + self.keywordToken('to') + valueRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line)

		projectName = match.group('name')
		key = match.group('key')
		value = match.group('value')

		settings = KeyValueSetting(key, value)
		settings.projectName = projectName

		return settings

	def isValidLine(self, line):
		regexpSrc = r'for\s+.*'+ self._command_token +r'\s+set'
		regexp = re.compile(regexpSrc, re.UNICODE)

		match = regexp.match(line)
		return match is not None