class LineConveyor:
	def __init__(self):
		self.processors = []

	def addProcessor(self, processor):
		assert processor is not None

		self.processors.append(processor)

	def processLine(self, line):
		assert line is not None

		for processor in self.processors:
			line = processor.processLine(line)

		return line
