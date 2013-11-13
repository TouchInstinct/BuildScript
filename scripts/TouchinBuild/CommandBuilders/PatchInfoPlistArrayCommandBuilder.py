from commands.PatchInfoPlistCommand import PatchInfoPlistCommand
from parsers.InsideParser.InsideSetArrayParser import InsideSetArrayParser


class PatchInfoPlistArrayCommandBuilder:
	def __init__(self):
		pass

	def isPatchInfoPlist(self, line):
		assert line is not None

		parser = self.createParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		parser = self.createParser()
		result = parser.parseLine(line)

		path = result[0]
		key = result[1]
		value = parser.values

		command = PatchInfoPlistCommand(path, key, value)
		return command

	def createParser(self):
		parser = InsideSetArrayParser('plist')
		return parser

