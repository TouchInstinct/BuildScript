from commands.DeleteBackupCommand import DeleteBackupCommand
from parser.BackupParser.DeleteBackupParser import DeleteBackupParser


class DeleteBackupCommandBuilder:
	def __init__(self, pathProvider):
		assert pathProvider is not None
		self.__pathProvider = pathProvider

	def isDeleteBackup(self, line):
		assert line is not None

		parser = DeleteBackupParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		assert line is not None

		parser = DeleteBackupParser()
		parser.parseLine(line)

		command = DeleteBackupCommand(self.__pathProvider)
		return command
