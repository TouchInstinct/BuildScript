import re
from parsers.LineParser import LineParser
from parsers.RegexpBuilder import RegexpBuilder


class SignApkParser(LineParser):
	def __init__(self):
		LineParser.__init__(self)

	def parseLine(self, line):
		assert line is not None

		filePathRegexp = r"'(?P<path>[./ a-zA-Z]+\.sln)'"
		slnConfigRegexp = r"'(?P<config>[a-zA-Z|]+)'"
		projectRegexp = r"(?P<project>[.a-zA-Z]+)$"

		rb = RegexpBuilder()
		rSrc = rb.startsWith('sign') + rb.than('android') + filePathRegexp + rb.keywordToken('for') + slnConfigRegexp +\
			   rb.keywordToken('project') + projectRegexp
		regexp = re.compile(rSrc, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, rSrc)

		path = match.group('path')
		slnConfig = match.group('config')
		project = match.group('project')

		return path, slnConfig, project

	def isValidLine(self, line):
		assert line is not None

		rb = RegexpBuilder()
		rSrc = rb.startsWith('sign') + rb.than('android')

		regexp = re.compile(rSrc, re.UNICODE)
		match = regexp.match(line)

		return match is not None