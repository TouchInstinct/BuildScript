from commands.CopyCommand import CopyCommand
from parser.InstallProfileParser import InstallProfileParser


class InstallProfileCommandBuilder:
	def __init__(self):
		pass

	def isInstallProfile(self, line):
		assert line is not None

		return line.startswith('install profile')

	def getCommandFor(self, line):
		assert line is not None
		
		parser = InstallProfileParser()
		cpArgs = parser.parseLine(line)

		command = CopyCommand(cpArgs)
		return command
