class CsprojSettingBase:
	def __init__(self, appName=None):
		self.appName = appName
		pass

	def apply(self, csproj):
		pass

	def _notNoneOrEmpty(self, string_statement):
		assert string_statement is not None and len(string_statement) > 0
