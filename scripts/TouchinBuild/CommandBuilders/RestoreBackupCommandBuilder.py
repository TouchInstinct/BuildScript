from commands.BaseBackupCommand.RestoreBackupCommand import RestoreBackupCommand
from parsers.ParserBackup.RestoreBackupParser import RestoreBackupParser


class RestoreBackupCommandBuilder:
	def __init__(self):
		pass

	def isRestoreBackup(self, line):
		assert line is not None

		parser = RestoreBackupParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		assert line is not None

		parser = RestoreBackupParser()
		backupArguments = parser.parseLine(line)

		command = RestoreBackupCommand(backupArguments)
		return command
