from commands.BaseBackupCommand.CreateBackupCommand import CreateBackupCommand
from parsers.ParserBackup.CreateBackupParser import CreateBackupParser


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
		parser.parseLine(line)

		command = CreateBackupCommand()
		return command
