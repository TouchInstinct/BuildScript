from utils import InfoPlistPatcher


class PatchInfoPlistCommand():
	def __init__(self, pathToPlist, key, value):
		assert pathToPlist is not None
		assert key is not None
		assert value is not None

		self.__pathToPlist = pathToPlist
		self.__key = key
		self.__value = value

	def execute(self):
		patcher = InfoPlistPatcher(self.__pathToPlist)

		dictionary = { self.__key : self.__value }
		patcher.AddOrReplace(dictionary)
