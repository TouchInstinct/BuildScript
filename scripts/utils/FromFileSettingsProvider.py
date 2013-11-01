from parser.SettingsParser.SettingsParser import SettingsParser


class FromFileSettingsProvider:
	def __init__(self):
		pass

	def fetchSettings(self):
		settingsFile = open('scripts/settings.txt')
		content = settingsFile.read()

		parser = SettingsParser()
		parser.parse(content)

		return parser.settings
