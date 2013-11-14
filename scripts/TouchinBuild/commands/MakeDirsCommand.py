from commands.ShTextCommand import ShTextCommand


class MakeDirsCommand(ShTextCommand):
	def __init__(self, path):
		assert path is not None
		self.path = path

		cmdText = "mkdir -p '{0}'".format(self.path)
		ShTextCommand.__init__(self, cmdText)