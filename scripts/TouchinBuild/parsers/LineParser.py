import abc


class LineParser:
	__metaclass__ = abc.ABCMeta

	def __init__(self):
		pass

	@abc.abstractmethod
	def parseLine(self, line):
		pass

	@abc.abstractmethod
	def isValidLine(self, line):
		return False

	def _guardMatch(self, match_object, source, regexpSource = None):
		if match_object is None:
			msg = 'Recognition exception: "{0}" for "{1}"'.format(source, regexpSource)
			raise Exception(msg)


