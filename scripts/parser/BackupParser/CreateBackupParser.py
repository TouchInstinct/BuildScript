from parser.BackupParser.CreateBackupArguments import CreateBackupArguments
from parser.LineParser import LineParser
import re

class CreateBackupParser(LineParser):
	def __init__(self):
		self.__createBackupArguments = CreateBackupArguments()

	def parseLine(self, line):
		assert line is not None

		folderNameRegexp = r"'(?P<folder>[^']+)'$"

		regexpSource = self.startsWithKeywordToken('create backup for') + folderNameRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		folderName = match.group('folder')
		self.__createBackupArguments.folderName = folderName

		return self.__createBackupArguments

	def isValidLine(self, line):
		assert line is not None

		isValid = line.startswith('create backup')
		return  isValid
