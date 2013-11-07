class SettingsMerger:
	def __init__(self):
		pass

	def merge(self, globalSettings, settingDescription):
		value = settingDescription['value']
		segments = settingDescription['segments']

		propPath = segments[0:-1]
		propName = segments[-1]

		settingsDict = self.getSettingsDictByPath(globalSettings, propPath)
		#self.overrideGuard(settingsDict, propName, propPath)

		settingsDict[propName] = value

	def getSettingsDictByPath(self, globalSettings, pathToSettingsDict):

		settingsDict = globalSettings
		for segment in pathToSettingsDict:

			if segment not in settingsDict:
				settingsDict[segment] = {}

			settingsDict = settingsDict[segment]

		return settingsDict

	#def overrideGuard(self, dictionary, key, path):
	#	if key in dictionary:
	#		pathStr = '.'.join(path)
	#		msg = 'settings with name {0} by path {1} already exists with value {3}'.format(key, dictionary[key], pathStr)
	#		raise Exception(msg)


