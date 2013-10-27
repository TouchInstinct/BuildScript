from parser.LineParser import LineParser
from parser.ProjectParser.ProjectSetting.AttribureSetting import AttributeSetting
from parser.ProjectParser.ProjectSetting.KeyValueSetting import KeyValueSetting
import re

class ProjectLineParser(LineParser):
	def __init__(self, value_provider, command_token):
		assert value_provider is not None

		self._value_provider = value_provider
		self._command_token = command_token

	def parseLine(self, line):
		LineParser.parseLine(line)
		ws = ' '
		cmd_name_regexp = "^(?P<cmd_name>{0})".format(self._command_token)
		app_regexp = r"(?P<app>app:\S+)"
		setting_regexp = r"(?P<setting>\S+ '[^']+')$"

		source = cmd_name_regexp + ws + app_regexp + ws + setting_regexp
		regexp = re.compile(source, re.UNICODE)

		match = regexp.search(line)
		self._guardMatch(match, line)

		cmd_name = match.group('cmd_name')
		self.__parseProjectStatement(cmd_name)

		app_statement = match.group('app')
		project_name = self.__parseAppStatement(app_statement)

		setting_statement = match.group('setting')
		setting = self.__parseSettingStatement(setting_statement)

		setting.projectName = project_name
		return setting

	def __parseProjectStatement(self, statement):
		pass

	def __parseAppStatement(self, statement):
		patt = r'app:(?P<app_name>\w+)'

		match = re.match(patt, statement)
		self._guardMatch(match, statement)

		return match.group('app_name')

	def __parseSettingStatement(self, statement):
		self.__guardSource(statement)

		if statement.startswith('key:'):
			result = self.__parseKeyValueStatement(statement)
		else:
			result = self.__parseAttributeStatement(statement)

		return result

	def __parseKeyValueStatement(self, statement):
		self.__guardSource(statement)
		patt = r"key:(?P<key>\w+) '(?P<value>[^']+)'"

		match = re.search(patt, statement)
		self._guardMatch(match, statement)

		key = match.group('key')
		value_link = match.group('value')
		value = self._value_provider.getValueFor(value_link)
		setting = KeyValueSetting(key, value)

		return setting

	def __parseAttributeStatement(self, statement):
		self.__guardSource(statement)
		patt = r"(?P<attribute_name>\w+) '(?P<attribute_value>[^']+)'"

		match = re.search(patt, statement)
		self._guardMatch(match, statement)

		attribute_name = match.group('attribute_name')
		value_link = match.group('attribute_value')
		attribute_value = self._value_provider.getValueFor(value_link)

		setting = AttributeSetting(attribute_name, attribute_value)
		return setting

	def __guardSource(self, source_text):
		assert source_text is not None and len(source_text) > 0