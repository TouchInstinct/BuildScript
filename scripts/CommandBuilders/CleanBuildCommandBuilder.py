from commands.CleanBuildCommands.BuildCommand import BuildCommand
from commands.CleanBuildCommands.CleanCommand import CleanCommand
from parser import CleanBuildParser


class CleanBuildCommandBuilder:
	def __init__(self, pathToBuildUtil,  commandToken):
		assert pathToBuildUtil is not None
		assert commandToken is not None

		self.__pathToBuildUtil = pathToBuildUtil
		self.__commandToken = commandToken

	def isCleanBuild(self, line):
		assert line is not None

		parser = CleanBuildParser(self.__commandToken)
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		assert line is not None

		parser = CleanBuildParser(self.__commandToken)
		result = parser.parseLine(line)

		slnPath = result[0]
		slnConf = result[1]

		command = self.__getCommandByToken(slnPath, slnConf)
		return command

	def __getCommandByToken(self, slnPath, slnConfig):
		if self.__commandToken == 'clean':
			command = CleanCommand(self.__pathToBuildUtil, slnPath, slnConfig)
		elif self.__commandToken == 'build':
			command = BuildCommand(self.__pathToBuildUtil, slnPath, slnConfig)
		else:
			raise Exception('unrecognised command token {0}'.format(self.__commandToken))

		return command