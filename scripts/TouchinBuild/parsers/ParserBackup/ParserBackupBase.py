from parsers.LineParser import LineParser


class ParserBackupBase(LineParser):
	def __init__(self):
		LineParser.__init__(self)

	def parseLine(self, line):
		assert line is not None

		mathInfo = self.getMatchInfo(line)
		match = mathInfo[0]
		regexpSource = mathInfo[1]

		self._guardMatch(match, line, regexpSource)

	def getMatchInfo(self, line):
		return None, None

	def isValidLine(self, line):
		assert line is not None

		matchInfo = self.getMatchInfo(line)
		match = matchInfo[0]

		return match is not None

