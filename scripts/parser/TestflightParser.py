from parser.LineParser import LineParser
import re

class TestflightParser(LineParser):
	def __init__(self):
		LineParser.__init__(self)

	def parseLine(self, line):
		assert line is not None

		notesRegexp = r"'(?P<notes>[^']+)'"
		apiTokenRegexp = r"'(?P<api_token>[^']+)'"
		teamTokenRegexp = r"'(?P<team_token>[^']+)'"
		filePathRegexp = r"'(?P<path>[^']+)'"

		regexpSource = self.startsWith('publish') + filePathRegexp + self.keywordToken('to') + self.than('testflight') + \
					   self.than('notes') + self.than('=') + notesRegexp + \
					   self.keywordToken('api_token') + self.than('=') + apiTokenRegexp + \
					   self.keywordToken('team_token') + self.than('=') + teamTokenRegexp

		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		path = match.group('path')
		notes = match.group('notes')
		apiToken = match.group('api_token')
		teamToken = match.group('team_token')

		return {
			'path': path,
			'notes': notes,
			'api_token': apiToken,
			'team_token': teamToken
		}

	def isValidLine(self, line):
		assert line is not None

		return line.startswith('publish')