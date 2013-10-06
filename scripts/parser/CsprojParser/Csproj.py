class Csproj:
	def __init__(self, appName):
		self.appName = appName
		self.settings = {}

	def __str__(self):
		return 'app Name: {0} settings: {1}'.format(self.appName, self.settings)