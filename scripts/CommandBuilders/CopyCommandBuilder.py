from commands.CopyCommand import CopyCommand
from parser.CopyParser.CopyLineParser import CopyLineParser


class CopyCommandBuilder:
	def __init__(self, pathProvider):
		assert pathProvider is not None

		self.__pathProvider = pathProvider

	def isCopy(self, line):
		assert line is not None

		return line.startswith('copy')

	def getCommandFor(self, line):
		assert line is not None

		parser = CopyLineParser()
		cpArg = parser.parseLine(line)

		command = CopyCommand(self.__pathProvider, cpArg)
		return command
