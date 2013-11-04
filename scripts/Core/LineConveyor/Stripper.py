class Stripper:
	def processLine(self, line):
		assert line is not None

		return line.strip(' \t\n\r')
