from parser.SettingsParser.SettingsParser import SettingsParser


class FromFileSettingsProvider:
	def fetchSettings(self):
		settingsFile = open('scripts/settings.txt')
		content = settingsFile.read()

		parser = SettingsParser()
		parser.parse(content)

		return parser.settings
