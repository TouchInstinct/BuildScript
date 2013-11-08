class Stripper:
	def __init__(self):
		pass

	def processText(self, line):
		assert line is not None

		return line.strip(' \t\n\r')
