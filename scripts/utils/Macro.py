import re

class Macro:
	def __init__(self, valueResolver):
		assert valueResolver is not None

		self.__valueResolver = valueResolver

	def resolveLine(self, line):
		assert line is not None

		symbols = self.getSymbols(line)

	def getSymbols(self, line):
		assert line is not None

		symRegexp = r"{@(?P<symbol>[\w]+)}"
		regexp = re.compile(symRegexp)

		result = regexp.findall(line)
		symbols = []
		if result is not None:
			for r in result:
				symbols.append(r)

		return symbols