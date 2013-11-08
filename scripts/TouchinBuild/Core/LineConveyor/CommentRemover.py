class CommentRemover:
	def __init__(self):
		pass

	def processText(self, line):
		assert line is not None

		newLine = line
		index = line.find('#')
		if index >= 0:
			newLine = line[:index]

		return newLine