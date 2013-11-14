from commands.PatchManifestCommand import PatchManifestCommand
from parsers.InsideParser.InsideSetParser import InsideSetParser


class PatchManifestCommandBuilder:
	def __init__(self):
		pass

	def isManifestCommand(self, line):
		assert line is not None

		parser = InsideSetParser('xml')
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		assert line is not None

		parser = InsideSetParser('xml')
		result = parser.parseLine(line)

		command = PatchManifestCommand(result[0], result[1], result[2])
		return command
