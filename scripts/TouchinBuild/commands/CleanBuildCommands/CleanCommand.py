from commands.CleanBuildCommands.CleanBuildCommandBase import CleanBuildCommandBase


class CleanCommand(CleanBuildCommandBase):
	def __init__(self, pathToBuildUtil, slnPath, slnConfig):
		commandPattern = '{0} -v build "--configuration:{1}" "--target:Clean" {2}'
		CleanBuildCommandBase.__init__(self, commandPattern, pathToBuildUtil, slnPath, slnConfig)
