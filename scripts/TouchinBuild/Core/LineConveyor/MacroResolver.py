class MacroResolver:
	def __init__(self, macroProcessor, valueProvider):
		assert macroProcessor is not None
		assert valueProvider is not None

		self.macroProcessor = macroProcessor
		self.valueProvider = valueProvider

	def processText(self, line, conveyorProcessor):
		assert line is not None

		symbols = self.macroProcessor.getSymbols(line)

		for sym in symbols:
			macro = self.macroProcessor.getMacroByName(sym)
			value = self.valueProvider.getValueFor(sym)

			line = line.replace(macro, value)

		return line