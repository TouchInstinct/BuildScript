class SettingsMerger:
	def __init__(self):
		pass

	def merge(self, globalSettings, settingDescription):
		value = settingDescription['value']
		segments = settingDescription['segments']

		propPath = segments[0:-1]
		propName = segments[-1]

		settingsDict = self.getSettingsDictByPath(globalSettings, propPath)
		settingsDict[propName] = value

	def getSettingsDictByPath(self, globalSettings, pathToSettingsDict):

		settingsDict = globalSettings
		for segment in pathToSettingsDict:

			if segment not in settingsDict:
				settingsDict[segment] = {}

			settingsDict = settingsDict[segment]

		return settingsDict