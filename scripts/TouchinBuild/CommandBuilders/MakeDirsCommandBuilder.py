from commands.MakeDirsCommand import MakeDirsCommand
from parsers.MakeDirsParser import MakeDirsParser


class MakeDirsCommandBuilder:
	def __init__(self):
		pass

	def isMakeDirsCommand(self, line):
		assert line is not None

		parser = MakeDirsParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		assert line is not None

		parser = MakeDirsParser()
		path = parser.parseLine(line)

		command = MakeDirsCommand(path)
		return command