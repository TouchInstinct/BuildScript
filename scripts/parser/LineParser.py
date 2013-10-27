class LineParser:
	def parseLine(self, line):
		assert line is not None
		pass

	def isValidLine(self, line):
		assert line is not None
		return False

	def _guardMatch(self, match_object, source, regexpSource = None):
		if match_object is None:
			msg = 'Recognition exception: {0} for {1}'.format(source, regexpSource)
			raise Exception(msg)


