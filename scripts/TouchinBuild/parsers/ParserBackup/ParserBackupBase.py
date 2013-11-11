import re

from parsers.LineParser import LineParser
from parsers.ParserBackup.BackupArguments import BackupArguments


class ParserBackupBase(LineParser):
	def __init__(self):
		LineParser.__init__(self)
		self.__backupArguments = BackupArguments()

	def parseLine(self, line):
		assert line is not None

		mathInfo = self.getMatchInfo(line)
		match = mathInfo[0]
		regexpSource = mathInfo[1]

		self._guardMatch(match, line, regexpSource)

		folderName = match.group('folder')
		self.__backupArguments.folderPath = folderName

		return self.__backupArguments

	def getMatchInfo(self, line):
		return None, None

	def isValidLine(self, line):
		assert line is not None

		matchInfo = self.getMatchInfo(line)
		match = matchInfo[0]

		return match is not None

