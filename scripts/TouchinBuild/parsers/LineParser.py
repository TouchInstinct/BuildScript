class LineParser:
	def __init__(self):
		pass

	def parseLine(self, line):
		assert line is not None
		pass

	def isValidLine(self, line):
		assert line is not None
		return False

	def keywordToken(self, keyword):
		assert keyword is not None
		return r'\s+' + keyword + r'\s+'

	def startsWith(self, keyword):
		assert keyword is not None
		return r'^' + keyword + r'\s+'

	def spaceEndsWith(self, keyword):
		assert keyword is not None
		return r'\s+' + keyword + '$'

	def endsWith(self, keyword):
		assert keyword is not None
		return keyword + '$'

	def than(self, keyword):
		assert keyword is not None
		return keyword + r'\s+'

	def _guardMatch(self, match_object, source, regexpSource = None):
		if match_object is None:
			msg = 'Recognition exception: "{0}" for "{1}"'.format(source, regexpSource)
			raise Exception(msg)


