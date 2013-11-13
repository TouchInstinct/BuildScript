from Core.LineConveyor.PreprocessorBase import PreprocessorBase


class TextConveyorPreprocessor(PreprocessorBase):
	def __init__(self):
		PreprocessorBase.__init__(self)
		self.processors = []

	def addProcessor(self, processor):
		assert processor is not None

		self.processors.append(processor)

	def processText(self, text, conveyorProcessor):
		assert text is not None

		for processor in self.processors:
			text = processor.processText(text, conveyorProcessor)

		return text
