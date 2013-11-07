from commands.CleanBuildCommands.CleanBuildCommandBase import CleanBuildCommandBase


class BuildCommand(CleanBuildCommandBase):
	def __init__(self, pathToBuildUtil, slnPath, slnConfig):
		commandPattern = '{0} -v build "--configuration:{1}" "--target:Build" {2}'
		CleanBuildCommandBase.__init__(self, commandPattern, pathToBuildUtil, slnPath, slnConfig)

