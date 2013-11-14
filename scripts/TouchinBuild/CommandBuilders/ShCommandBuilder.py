from commands.ShTextCommand import ShTextCommand
from parsers.ShParser import ShParser


class ShCommandBuilder:
	def __init__(self):
		pass

	def isShCommand(self, line):
		assert line is not None

		parser = ShParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		parser = ShParser()

		cmdText = parser.parseLine(line)

		command = ShTextCommand(cmdText)
		return command
