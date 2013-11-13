import os
from Core.SettingsProviderBase import SettingsProviderBase
from parsers.SettingsParser.SettingsParser import SettingsParser


class FromFileSettingsProvider(SettingsProviderBase):
	def __init__(self, pathToSettings, compositeLineProcessor):
		SettingsProviderBase.__init__(self)

		assert pathToSettings is not None
		assert compositeLineProcessor is not None

		self.pathToSettings = pathToSettings
		self.compositeLineProcessor = compositeLineProcessor

	def fetchSettings(self):
		if not os.path.exists(self.pathToSettings):
			raise Exception('settings file {0} not found'.format(self.pathToSettings))

		if not os.path.isfile(self.pathToSettings):
			raise Exception('{0} is not a file'.format(self.pathToSettings))

		settingsFile = open(self.pathToSettings)
		content = settingsFile.read()

		parser = SettingsParser(self.compositeLineProcessor, None)
		parser.parse(content)

		return parser.settings
