from commands.BaseBackupCommand.DeleteBackupCommand import DeleteBackupCommand
from parsers.ParserBackup.DeleteBackupParser import DeleteBackupParser


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
		folderPath = parser.parseLine(line)

		command = DeleteBackupCommand(folderPath)
		return command
