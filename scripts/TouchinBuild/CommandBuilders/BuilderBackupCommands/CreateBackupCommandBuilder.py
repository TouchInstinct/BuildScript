from CommandBuilders.BuilderBackupCommands.BaseBackupCommandBuilder import BaseBackupCommandBuilder
from commands.BaseBackupCommand.CreateBackupCommand import CreateBackupCommand
from parsers.ParserBackup.CreateBackupParser import CreateBackupParser


class CreateBackupCommandBuilder(BaseBackupCommandBuilder):
	def __init__(self, ignoreBackupStr):
		BaseBackupCommandBuilder.__init__(self, ignoreBackupStr)

	def isCreateBackup(self, line):
		assert line is not None

		parser = CreateBackupParser()
		return parser.isValidLine(line)

	def getCommandFor(self, line):
		assert line is not None

		parser = CreateBackupParser()
		parser.parseLine(line)

		command = CreateBackupCommand(self.ignoreBackup)
		return command
