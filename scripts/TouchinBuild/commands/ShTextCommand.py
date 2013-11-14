from commands.ShellCommandBase import ShellCommandBase


class ShTextCommand(ShellCommandBase):
	def __init__(self, commandText):
		ShellCommandBase.__init__(self)
		assert commandText is not None

		self.commandText = commandText

	def execute(self):
		self.executeShell(self.commandText)