__author__ = 'rzaitov'


class CopyArguments():
	def __init__(self):
		self.__source = None
		self.__target = None

	def setArguments(self, source, target):
		self.__source = source
		self.__target = target

	def isValid(self):
		result = self.__source is not None
		result &= self.__target is not None

		return  result