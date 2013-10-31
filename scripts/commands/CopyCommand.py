import shutil
import os

class CopyCommand:
	def __init__(self, pathProvider, copyArguments):
		assert pathProvider is not None
		assert copyArguments is not None

		self.__pathProvider = pathProvider
		self.__copyArguments = copyArguments

	def execute(self):
		source = self.__expandPath(self.__copyArguments.source)
		target = self.__expandPath(self.__copyArguments.target)

		shutil.copy(source, target)

	def __expandPath(self, path):
		path = os.path.expanduser(path)
		if not os.path.isabs(path):
			path = self.__pathProvider.resolveAbsPath(path)

		return path


