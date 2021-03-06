from parsers.LineParser import LineParser
import re
from parsers.RegexpBuilder import RegexpBuilder


class TestflightParser(LineParser):
	def __init__(self):
		LineParser.__init__(self)

	def parseLine(self, line):
		assert line is not None

		rb = RegexpBuilder()

		notesRegexp = r"'(?P<notes>[^']+)'"
		apiTokenRegexp = r"'(?P<api_token>[^']+)'"
		teamTokenRegexp = r"'(?P<team_token>[^']+)'"
		filePathRegexp = r"'(?P<path>[^']+)'"

		regexpSource = rb.startsWith('publish') + filePathRegexp + rb.keywordToken('to') + rb.than('testflight') + \
					   rb.than('notes') + rb.than('=') + notesRegexp + \
					   rb.keywordToken('api_token') + rb.than('=') + apiTokenRegexp + \
					   rb.keywordToken('team_token') + rb.than('=') + teamTokenRegexp

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