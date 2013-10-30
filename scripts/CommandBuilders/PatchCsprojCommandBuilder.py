from commands.PatchCsprojCommand import PatchCsprojCommand
from parser.ProjectParser.InsideParser import InsideParser


class PatchCsprojCommandBuilder:
	def __init__(self, config,  pathProvider, valueProvider):
		assert config is not None
		assert pathProvider is not None
		assert valueProvider is not None

		self.__config = config
		self.__pathProvider = pathProvider
		self.__valueProvider = valueProvider

	def getCommandFor(self, line):
		assert line is not None

		parser = InsideParser(self.__valueProvider, 'csproj')
		result = parser.parseLine(line)

		relPath = result[0]
		key = result[1]
		value = self.__valueProvider.getValueFor(result[2])

		csprojAbsPath = self.__valueProvider.resolveAbsPath(relPath)
		slnConfig = self.__config['sln_config']

		command = PatchCsprojCommand(csprojAbsPath, key, value, slnConfig)
		return command
