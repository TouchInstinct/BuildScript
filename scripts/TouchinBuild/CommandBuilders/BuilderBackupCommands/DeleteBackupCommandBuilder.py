from CommandBuilders.BuilderBackupCommands.BaseBackupCommandBuilder import BaseBackupCommandBuilder
from commands.BaseBackupCommand.DeleteBackupCommand import DeleteBackupCommand
from parsers.ParserBackup.DeleteBackupParser import DeleteBackupParser


class DeleteBackupCommandBuilder(BaseBackupCommandBuilder):
	def __init__(self, ignoreBackupStr):
		BaseBackupCommandBuilder.__init__(self, ignoreBackupStr)

	def isDeleteBackup(self, line):
		assert line is not None

		parser = DeleteBackupParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		assert line is not None

		parser = DeleteBackupParser()
		parser.parseLine(line)

		command = DeleteBackupCommand(self.ignoreBackup)
		return command
