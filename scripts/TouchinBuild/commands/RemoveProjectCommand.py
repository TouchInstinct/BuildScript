from commands.CommandBase import CommandBase
from utils.SlnPatcher import SlnPatcher


class RemoveProjectCommand(CommandBase):
	def __init__(self, slnPath, projectNames):
		CommandBase.__init__(self)

		assert slnPath is not None
		assert projectNames is not None

		self.__slnPath = slnPath
		self.projectNames = projectNames

	def execute(self):
		patcher = SlnPatcher(self.__slnPath)
		patcher.removeProjects(self.projectNames)
