from subprocess import call


class ShCommand:
	def __init__(self, commandText):
		assert commandText is not None

		self.__commandText = commandText

	def execute(self):
		call(self.__commandText, shell=True)
