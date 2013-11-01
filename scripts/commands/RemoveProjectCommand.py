from utils.sln.Patcher import Patcher


class RemoveProjectCommand:
	def __init__(self, slnPath, projectName):
		assert slnPath is not None
		assert projectName is not None

		self.__slnPath = slnPath
		self.__projectName = projectName

	def execute(self):
		patcher = Patcher(self.__slnPath)
		patcher.removeProjects([self.__projectName])
