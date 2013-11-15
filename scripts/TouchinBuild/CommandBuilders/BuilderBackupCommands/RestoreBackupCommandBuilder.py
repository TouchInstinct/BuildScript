from CommandBuilders.BuilderBackupCommands.BaseBackupCommandBuilder import BaseBackupCommandBuilder
from commands.BaseBackupCommand.RestoreBackupCommand import RestoreBackupCommand
from parsers.ParserBackup.RestoreBackupParser import RestoreBackupParser


class RestoreBackupCommandBuilder(BaseBackupCommandBuilder):
	def __init__(self, ignoreBackupStr):
		BaseBackupCommandBuilder.__init__(self, ignoreBackupStr)

	def isRestoreBackup(self, line):
		assert line is not None

		parser = RestoreBackupParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		assert line is not None

		parser = RestoreBackupParser()
		parser.parseLine(line)

		command = RestoreBackupCommand(self.ignoreBackup)
		return command
