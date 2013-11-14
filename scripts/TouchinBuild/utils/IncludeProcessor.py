import re
from parsers.RegexpBuilder import RegexpBuilder


class IncludeProcessor:
	def __init__(self):
		pass

	def getIncludesInfo(self, text):
		assert text is not None

		rb = RegexpBuilder()
		regexpSource = '<\s*' + rb.than('include') + r"'[^']+'" + '\s*>'

		regexp = re.compile(regexpSource, re.UNICODE)
		results = regexp.findall(text)

		includesInfo = []
		if results:
			for r in results:
				path = self.getPathByIncludeStatement(r)
				includesInfo.append((r, path))

		return includesInfo

	def getPathByIncludeStatement(self, includeStatement):
		assert includeStatement is not None

		regexpSource = r"'([^']+)'"
		regexp = re.compile(regexpSource, re.UNICODE)

		results = regexp.findall(includeStatement)
		path = results[0]

		return path