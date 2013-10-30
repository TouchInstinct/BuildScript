from commands.ShCommand import ShCommand


class MakeDirsCommand:
	def __init__(self, path):
		assert path is not None

		self.__path = path

	def execute(self):
		cmdText = "mkdir -p '{0}'".format(self.__path)
		innerCommand = ShCommand(cmdText)
		innerCommand.execute()
