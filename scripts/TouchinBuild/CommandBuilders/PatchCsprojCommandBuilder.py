from commands.PatchCsprojCommand import PatchCsprojCommand
from parsers.InsideParser.InsideCsprojSetParser import InsideCsprojSetParser


class PatchCsprojCommandBuilder:
	def __init__(self):
		pass

	def getCommandFor(self, line):
		assert line is not None

		parser = self.getParser()
		result = parser.parseLine(line)

		csprojPath = result[0]
		key = result[1]
		value = result[2]
		slnConfig = result[3]

		command = PatchCsprojCommand(csprojPath, key, value, slnConfig)
		return command

	def isPatchCsproj(self, line):
		assert line is not None

		parser = self.getParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getParser(self):
		return InsideCsprojSetParser('csproj')