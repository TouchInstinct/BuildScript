import abc
from parsers.LineParser import LineParser


class InsideParserBase(object, LineParser):
	__metaclass__ = abc.ABCMeta

	def __init__(self, fileExt):
		LineParser.__init__(self)

		assert fileExt is not None
		self.fileExt = fileExt
		self.filePathRegexp = r"'(?P<file>[./ a-zA-Z]+\.{0})'".format(self.fileExt)

	@abc.abstractmethod
	def getMatchInfo(self, line):
		# "Not implemented"
		return None, None

	def fetchMatchFor(self, text):
		assert text is not None

		matchInfo = self.getMatchInfo(text)
		match = matchInfo[0]
		regexpSource = matchInfo[1]

		self._guardMatch(match, text, regexpSource)

		return match


	def isValidLine(self, line):
		assert line is not None

		matchInfo = self.getMatchInfo(line)
		match = matchInfo[0]

		return match is not None
