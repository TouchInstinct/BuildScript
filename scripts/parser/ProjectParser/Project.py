class Project:
	def __init__(self, projectName):
		self.projectName = projectName
		self.settings = {}

	def __str__(self):
		return 'app Name: {0} settings: {1}'.format(self.projectName, self.settings)