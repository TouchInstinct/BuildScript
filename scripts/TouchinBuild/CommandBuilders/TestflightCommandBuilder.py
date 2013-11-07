from commands.TestflightCommand import TestflightCommand
from parsers.TestflightParser import TestflightParser


class TestflightCommandBuilder:
	def __init__(self):
		pass

	def isTestflight(self, line):
		assert line is not None

		parser = TestflightParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		assert line is not None

		parser = TestflightParser()
		result = parser.parseLine(line)

		command = TestflightCommand(result['path'], result['api_token'], result['team_token'], result['notes'])
		return command