import utils.csproj.Patcher as csproj

class PatchCsprojCommand():
	def __init__(self, csprojAbsPath, key, value, slnConfig):
		assert csprojAbsPath is not None
		assert key is not None
		assert value is not None
		assert slnConfig is not None

		self.__csprojAbsPath = csprojAbsPath
		self.__key = key
		self.__value = value
		self.__slnConfig = slnConfig

	def execute(self):
		patcher = csproj.Patcher(self.__csprojAbsPath)

		dictionary = { self.__key : self.__value }
		patcher.AddOrReplace(dictionary, self.__slnConfig)