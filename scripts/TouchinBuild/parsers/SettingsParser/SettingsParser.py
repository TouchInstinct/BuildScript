from parsers.SettingsParser.SettingsLineParser import SettingsLineParser
from parsers.SettingsParser.SettingsMerger import SettingsMerger


class SettingsParser:
	def __init__(self, compositeLineProcessor, settings=None):
		assert compositeLineProcessor is not None

		self.compositeLineProcessor = compositeLineProcessor

		self.settings = settings
		if self.settings is None:
			self.settings = {}

	def parse(self, content):
		assert content is not None

		lines = content.splitlines()
		for line in lines:
			processedLine = self.compositeLineProcessor.processText(line, None)

			if len(processedLine) == 0:
				continue
			else:
				self.processLine(processedLine)

	def processLine(self, line):
		assert line is not None

		parser = SettingsLineParser()
		setting = parser.parseLine(line)

		self.mergeSetting(setting)

	def mergeSetting(self, settingDescription):
		merger = SettingsMerger()
		merger.merge(self.settings, settingDescription)