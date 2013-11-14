class RegexpBuilder:
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