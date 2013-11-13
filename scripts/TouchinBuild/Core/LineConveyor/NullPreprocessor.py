from Core.LineConveyor.PreprocessorBase import PreprocessorBase


class NullPreprocessor(PreprocessorBase):
	def __init__(self):
		PreprocessorBase.__init__(self)

	def processText(self, text, conveyorProcessor):
		return text
