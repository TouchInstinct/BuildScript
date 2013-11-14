from commands.CommandBase import CommandBase
from subprocess import call


class ShellCommandBase(CommandBase):
	def __init__(self):
		CommandBase.__init__(self)

	def executeShell(self, commandText):
		assert commandText is not None

		retCode = call(commandText, shell=True)

		if retCode != 0:
			msg = 'problem with shell command: {0}'.format(commandText)
			raise Exception(msg)