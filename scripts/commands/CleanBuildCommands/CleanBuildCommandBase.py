from subprocess import call


class CleanBuildCommandBase:
	def __init__(self, commandPattern, pathToBuildUtil, slnPath, slnConfig):
		assert commandPattern is not None
		assert pathToBuildUtil is not None
		assert slnPath is not None
		assert slnConfig is not None

		self.__commandPattern = commandPattern
		self.__pathToBuildUtil = pathToBuildUtil
		self.__slnPath = slnPath
		self.__slnConfig = slnConfig

	def execute(self):
		cleanCmdText = self.__commandPattern.format(self.__pathToBuildUtil, self.__slnConfig, self.__slnPath)
		returnCode = call(cleanCmdText, shell=True)
