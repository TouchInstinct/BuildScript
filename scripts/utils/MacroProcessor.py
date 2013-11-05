import re

class MacroProcessor:
	def __init__(self):
		pass

	def getMacroByName(self, macroName):
		assert macroName is not None
		assert macroName.startswith('@')

		return '{' + macroName + '}'

	def getMacroName(self, macro):
		assert macro.startswith('{@')
		assert macro.endswith('}')

		return macro[1:-1]

	def getSymbols(self, line):
		assert line is not None

		symRegexp = r"{(?P<symbol>@[\w]+)}"
		regexp = re.compile(symRegexp)

		result = regexp.findall(line)
		symbols = []
		if result is not None:
			for r in result:
				symbols.append(r)

		return symbols