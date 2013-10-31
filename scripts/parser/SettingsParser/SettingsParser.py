from parser.SettingsParser.SettingsLineParser import SettingsLineParser


class SettingsParser:
	def __init__(self):
		self.settings = {}

	def parse(self, content):
		assert content is not None

		lines = content.splitlines()
		for line in lines:
			self.processLine(line)

	def processLine(self, line):

		parser = SettingsLineParser()
		result = parser.parseLine(line)

	def mergeSetting(self, setting):
		value = setting['value']
		segments = setting['segments']

		propPath = segments[0:-1]
		propName = segments[-1]

		settingsDict = self.getSettingsDictByPath(propPath)
		self.overrideGuard(settingsDict, propName, propPath)

		settingsDict[propName] = value

	def getSettingsDictByPath(self, pathToSettingsDict):

		settingsDict = self.settings
		for segment in pathToSettingsDict:

			if segment not in settingsDict:
				settingsDict[segment] = {}

			settingsDict = settingsDict[segment]

		return settingsDict

	def overrideGuard(self, dict, key, path):
		if key in dict:
			pathStr = '.'.joun(path)
			msg = 'settings with name {0} by path {1} already exists with value {3}'.format(key, dict[key], pathStr)
			raise Exception(msg)

