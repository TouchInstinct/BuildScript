from commands.CreateBackupCommand import CreateBackupCommand
from parser.BackupParser.CreateBackupParser import CreateBackupParser


class CreateBackupCommandBuilder:
	def __init__(self):
		pass

	def isCreateBackup(self, line):
		assert line is not None

		parser = CreateBackupParser()
		return parser.isValidLine(line)

	def getCommandFor(self, line):
		assert line is not None

		parser = CreateBackupParser()
		backupArguments = parser.parseLine(line)

		command = CreateBackupCommand(backupArguments)
		return command
