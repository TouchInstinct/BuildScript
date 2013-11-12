from parsers.LineParser import LineParser


class ParserBackupBase(LineParser):
	def __init__(self):
		LineParser.__init__(self)
		self.folderName = None

	def parseLine(self, line):
		assert line is not None

		mathInfo = self.getMatchInfo(line)
		match = mathInfo[0]
		regexpSource = mathInfo[1]

		self._guardMatch(match, line, regexpSource)

		folderName = match.group('folder')
		self.folderName = folderName

		return self.folderName

	def getMatchInfo(self, line):
		return None, None

	def isValidLine(self, line):
		assert line is not None

		matchInfo = self.getMatchInfo(line)
		match = matchInfo[0]

		return match is not None

