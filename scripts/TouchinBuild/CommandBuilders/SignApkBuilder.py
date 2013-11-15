from commands.CleanBuildCommands.SignApkCommand import SignApkCommand
from parsers.SignApkParser import SignApkParser


class SignApkCommandBuilder:
	def __init__(self, pathToBuildUtil):
		assert pathToBuildUtil is not None

		self.pathToBuildUtil = pathToBuildUtil

	def isSignApk(self, line):
		assert line is not None

		parser = SignApkParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		assert line is not None

		parser = SignApkParser()
		result = parser.parseLine(line)

		slnPath = result[0]
		slnConfig = result[1]
		projectName = result[2]

		command = SignApkCommand(self.pathToBuildUtil, slnPath, slnConfig, projectName)
		return command