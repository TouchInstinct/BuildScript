class TextInclude:
	def __init__(self, includeProcessor, contentProvider):
		assert includeProcessor is not None
		assert contentProvider is not None

		self.includeProcessor = includeProcessor
		self.contentProvider = contentProvider

	def processText(self, text, conveyorProcessor):
		assert text is not None
		includesInfo = self.includeProcessor.getIncludesInfo(text)

		for info in includesInfo:
			includeStatement = info[0]
			path = info[1]

			content = self.contentProvider.fetchContent(path)
			content = conveyorProcessor.processText(content, conveyorProcessor)

			text = text.replace(includeStatement, content)

		return text