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

	def getSafeSource(self):
		safeSource = self.__makeSafe(self.source)
		return safeSource

	def getSaveTarget(self):
		safeTarget = self.__makeSafe(self.target)
		return safeTarget

	def __makeSafe(self, filePath):
		assert filePath is not None

		safe = filePath if ' ' not in filePath else '"{0}"'.format(filePath)
		return safe