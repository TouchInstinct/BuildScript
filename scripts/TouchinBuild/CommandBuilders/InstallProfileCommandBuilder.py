import os
from commands.CopyCommand import CopyCommand
from parsers.CopyParser.CopyArguments import CopyArguments
from parsers.InstallProfileParser import InstallProfileParser


class InstallProfileCommandBuilder:
	def __init__(self, profileFilePrefix):
		assert profileFilePrefix is not None

		self.profileFilePrefix = profileFilePrefix
		self.profileStorageDir = '~/Library/MobileDevice/Provisioning Profiles/'

	def isInstallProfile(self, line):
		assert line is not None

		parser = InstallProfileParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		assert line is not None

		parser = InstallProfileParser()

		srcPath = parser.parseLine(line)
		dstPath = self.getDestinationPath(srcPath)

		cpArgs = CopyArguments()
		cpArgs.setArguments(srcPath, dstPath)

		command = CopyCommand(cpArgs)
		return command

	def getDestinationPath(self, sourcePath):
		dstProfileFileName = self.fetchDstFileName(sourcePath)
		dstProfilePath = os.path.join(self.profileStorageDir, dstProfileFileName)

		return dstProfilePath

	def fetchDstFileName(self, srcFilePath):
		profileFileName = os.path.basename(srcFilePath)
		profileFileName = '{0}.{1}'.format(self.profileFilePrefix, profileFileName)

		return profileFileName
