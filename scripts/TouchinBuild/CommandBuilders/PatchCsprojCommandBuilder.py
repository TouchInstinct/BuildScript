from commands.PatchCsprojCommand import PatchCsprojCommand
from parsers.InsideParser.InsideSetParser import InsideSetParser


class PatchCsprojCommandBuilder:
	def __init__(self, config, valueProvider):
		assert config is not None
		assert valueProvider is not None

		self.__config = config
		self.__valueProvider = valueProvider

	def getCommandFor(self, line):
		assert line is not None

		parser = InsideSetParser('csproj')
		result = parser.parseLine(line)

		csprojPath = result[0]
		key = result[1]
		value = self.__valueProvider.getValueFor(result[2])

		slnConfig = self.__config['sln_config']

		command = PatchCsprojCommand(csprojPath, key, value, slnConfig)
		return command

	def isPatchCsproj(self, line):
		assert line is not None

		parser = InsideSetParser('csproj')
		isValid = parser.isValidLine(line)

		return isValid

