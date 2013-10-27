import shutil

class CopyCommand:
	def __init__(self, pathProvider, copyArguments):
		assert pathProvider is not None
		assert copyArguments is not None

		self.__pathProvider = pathProvider
		self.__copyArguments =  copyArguments

	def execute(self):
		shutil.copy(self.__copyArguments.source, self.__copyArguments.target)

