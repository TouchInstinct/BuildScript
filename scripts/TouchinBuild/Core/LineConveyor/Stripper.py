from Core.LineConveyor.PreprocessorBase import PreprocessorBase


class Stripper(PreprocessorBase):
	def __init__(self):
		PreprocessorBase.__init__(self)

	def processText(self, line, conveyorProcessor):
		assert line is not None

		return line.strip(' \t\n\r')
