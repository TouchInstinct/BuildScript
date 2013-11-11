from Core.SettingsProviderBase import SettingsProviderBase
from parsers.SettingsParser.SettingsParser import SettingsParser


class SettingsProviderStub(SettingsProviderBase):
	def __init__(self, settingsText):
		assert settingsText is not None

		SettingsProviderBase.__init__(self)
		self.settingsText = settingsText

	def fetchSettings(self):
		parser = SettingsParser()
		parser.parse(self.settingsText)

		return parser.settings