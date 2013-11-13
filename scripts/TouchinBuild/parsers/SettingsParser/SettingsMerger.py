class SettingsMerger:
	def __init__(self):
		pass

	def merge(self, globalSettings, settingDescription):
		value = settingDescription['value']
		segments = settingDescription['segments']

		propPath = self.getPath(segments)
		propName = self.getPropertyName(segments)

		settingsDict = self.getSettingsDictByPath(globalSettings, propPath)
		settingsDict[propName] = value

	def getSettingsDictByPath(self, globalSettings, pathToSettingsDict):

		settingsDict = globalSettings
		for segment in pathToSettingsDict:

			if segment not in settingsDict:
				settingsDict[segment] = {}

			settingsDict = settingsDict[segment]

		return settingsDict

	def getPath(self, segments):
		assert segments is not None
		return segments[0:-1]

	def getPropertyName(self, segments):
		assert segments is not None
		return segments[-1]