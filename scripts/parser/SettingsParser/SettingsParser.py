from parser.SettingsParser.SettingsLineParser import SettingsLineParser
from parser.SettingsParser.SettingsMerger import SettingsMerger


class SettingsParser:
	def __init__(self, settings=None):
		self.settings = settings

		if not self.settings:
			self.settings = {}

	def parse(self, content):
		assert content is not None

		lines = content.splitlines()
		for line in lines:
			stripped = line.strip(' \t\n\r')

			if len(stripped) == 0:
				continue
			if stripped.startswith("#"):
				continue

			self.processLine(stripped)

	def processLine(self, line):
		assert line is not None

		parser = SettingsLineParser()
		setting = parser.parseLine(line)

		self.mergeSetting(setting)

	def mergeSetting(self, settingDescription):
		merger = SettingsMerger()
		merger.merge(self.settings, settingDescription)