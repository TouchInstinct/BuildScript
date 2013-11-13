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
		settingsFile = open(self.pathToSettings)
		content = settingsFile.read()

		parser = SettingsParser(self.compositeLineProcessor, None)
		parser.parse(content)

		return parser.settings
