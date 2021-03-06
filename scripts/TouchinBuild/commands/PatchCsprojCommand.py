from commands.CommandBase import CommandBase
import utils.CsprojPatcher as csproj

class PatchCsprojCommand(CommandBase):
	def __init__(self, csprojAbsPath, key, value, slnConfig):
		CommandBase.__init__(self)

		assert csprojAbsPath is not None
		assert key is not None
		assert value is not None
		assert slnConfig is not None

		self.__csprojAbsPath = csprojAbsPath
		self.__key = key
		self.__value = value
		self.__slnConfig = slnConfig

	def execute(self):
		patcher = csproj.CsprojPatcher(self.__csprojAbsPath)

		dictionary = { self.__key : self.__value }
		patcher.AddOrReplace(dictionary, self.__slnConfig)