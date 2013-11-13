from Core.LineConveyor.PreprocessorBase import PreprocessorBase


class CommentRemover(PreprocessorBase):
	def __init__(self):
		PreprocessorBase.__init__(self)

	def processText(self, line, conveyorProcessor):
		assert line is not None

		newLine = line
		index = line.find('#')
		if index >= 0:
			newLine = line[:index]

		return newLine