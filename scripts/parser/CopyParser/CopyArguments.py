__author__ = 'rzaitov'


class CopyArguments():
	def __init__(self):
		self.source = None
		self.target = None

	def setArguments(self, source, target):
		self.source = source
		self.target = target

	def isValid(self):
		result = self.source is not None
		result &= self.target is not None

		return  result