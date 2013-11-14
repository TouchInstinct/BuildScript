import unittest
from commands.ShellCommandBase import ShellCommandBase


class MyShellCommand(ShellCommandBase):
	def __init__(self, execWithError=False):
		ShellCommandBase.__init__(self)
		self.execWithError = execWithError

	def execute(self):
		cmdText = 'exit 1' if self.execWithError else 'exit 0'
		self.executeShell(cmdText)


class TestShellCommand(unittest.TestCase):
	def test_noError(self):
		cmd = MyShellCommand(execWithError=False)
		cmd.execute()

	def test_withError(self):
		cmd = MyShellCommand(execWithError=True)

		with self.assertRaises(Exception):
			cmd.execute()