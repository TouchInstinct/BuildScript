import os
from parser.SettingsParser.SettingsParser import SettingsParser


class FromFileSettingsProvider:
	def fetchSettings(self):
		settingsFile = open('settings.txt')
		content = settingsFile.read()

		parser = SettingsParser()
		parser.parse(content)

		return parser.settings
