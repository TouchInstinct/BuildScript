import shutil
import os
from commands.CommandBase import CommandBase


class CopyCommand(CommandBase):
	def __init__(self, copyArguments):
		CommandBase.__init__(self)

		assert copyArguments is not None

		self.__copyArguments = copyArguments

	def execute(self):
		source = self.__expandPath(self.__copyArguments.source)
		target = self.__expandPath(self.__copyArguments.target)

		shutil.copy(source, target)

	def __expandPath(self, path):
		path = os.path.expanduser(path)
		return path


