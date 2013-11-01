from commands.ShCommand import ShCommand
from parser.ShParser import ShParser


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

		command = ShCommand(cmdText)
		return command
