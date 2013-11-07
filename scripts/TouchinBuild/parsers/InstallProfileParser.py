import re
import os
from parsers.CopyParser.CopyArguments import CopyArguments
from parsers.LineParser import LineParser


class InstallProfileParser(LineParser):
	def __init__(self):
		LineParser.__init__(self)
		self.__copyArguments = CopyArguments()
		self.__profileStorageDir = '~/Library/MobileDevice/Provisioning Profiles/'

	def parseLine(self, line):
		assert line is not None

		profilePathRegexp = r"'(?P<path>[^']+)'$"
		regexpSource = self.startsWith('install') + self.than('profile') + profilePathRegexp

		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		srcPath = match.group('path')
		dstPath = self.getDestinationPath(srcPath)

		self.__copyArguments.setArguments(srcPath, dstPath)
		return self.__copyArguments

	def getDestinationPath(self, sourcePath):
		profileFileName = os.path.basename(sourcePath)
		destination = os.path.join(self.__profileStorageDir, profileFileName)

		return destination