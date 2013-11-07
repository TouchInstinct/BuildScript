from commands.RestoreBackupCommand import RestoreBackupCommand
from parsers.BackupParser.RestoreBackupParser import RestoreBackupParser


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
		parser.parseLine(line)

		command = RestoreBackupCommand()
		return command
