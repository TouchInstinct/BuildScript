class Stripper:
	def processText(self, line):
		assert line is not None

		return line.strip(' \t\n\r')
