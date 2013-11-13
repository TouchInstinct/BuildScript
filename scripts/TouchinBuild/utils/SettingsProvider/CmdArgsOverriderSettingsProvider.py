from Core.SettingsProviderBase import SettingsProviderBase
from parsers.SettingsParser.SettingsParser import SettingsParser


class CmdArgsOverriderSettingsProvider(SettingsProviderBase):
	def __init__(self, settingsProvider, settingLines, compositeLineProcessor):
		SettingsProviderBase.__init__(self)
		assert settingsProvider is not None
		assert compositeLineProcessor is not None

		self.inner = settingsProvider
		self.overrideSettings = settingLines
		self.compositeLineProcessor = compositeLineProcessor

	def fetchSettings(self):
		settings = self.inner.fetchSettings()

		if self.overrideSettings:
			for s in self.overrideSettings:
				line = self.normalizeLine(s)
				settingParser = SettingsParser(self.compositeLineProcessor, settings)
				settingParser.processLine(line)

		return settings


	def normalizeLine(self, line):
		assert line is not None
		assert '=' in line

		index = line.find('=')
		path = line[0:index]
		value = line[index + 1:]

		normalizedLine = "{0} = '{1}'".format(path, value)
		return normalizedLine
