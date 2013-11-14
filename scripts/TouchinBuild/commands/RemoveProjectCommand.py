from commands.CommandBase import CommandBase
from utils.SlnPatcher import SlnPatcher


class RemoveProjectCommand(CommandBase):
	def __init__(self, slnPath, projectName):
		CommandBase.__init__(self)

		assert slnPath is not None
		assert projectName is not None

		self.__slnPath = slnPath
		self.__projectName = projectName

	def execute(self):
		patcher = SlnPatcher(self.__slnPath)
		patcher.removeProjects([self.__projectName])
