from commands.DeleteBackupCommand import DeleteBackupCommand
from parser.BackupParser.DeleteBackupParser import DeleteBackupParser


class DeleteBackupCommandBuilder:
	def __init__(self):
		pass

	def isDeleteBackup(self, line):
		assert line is not None

		parser = DeleteBackupParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		assert line is not None

		parser = DeleteBackupParser()
		parser.parseLine(line)

		command = DeleteBackupCommand()
		return command
