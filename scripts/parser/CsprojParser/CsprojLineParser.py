from parser.CsprojParser.CsprojSetting.AttribureSetting import AttributeSetting
from parser.CsprojParser.CsprojSetting.KeyValueSetting import KeyValueSetting
import re

class CsprojLineParser:
	def parse(self, line):
		ws = ' '
		csproj_regexp = "^(?P<cmd_name>csproj)"
		app_regexp = r"(?P<app>app:\S+)"
		setting_regexp = r"(?P<setting>\S+ '[^']+')$"

		source = csproj_regexp + ws + app_regexp + ws + setting_regexp
		regexp = re.compile(source, re.UNICODE)

		match = regexp.search(line)
		self.__guardMatch(match, line)

		cmd_name = match.group('cmd_name')
		self.__parseCsprojStatement(cmd_name)

		app_statement = match.group('app')
		appName = self.__parseAppStatement(app_statement)

		setting_statement = match.group('setting')
		setting = self.__parseSettingStatement(setting_statement)

		setting.appName = appName
		return setting

	def __parseCsprojStatement(self, statement):
		pass

	def __parseAppStatement(self, statement):
		patt = r'app:(?P<app_name>\w+)'

		match = re.match(patt, statement)
		self.__guardMatch(match, statement)

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
		self.__guardMatch(match, statement)

		key = match.group('key')
		value = match.group('value')
		setting = KeyValueSetting(key, value)

		return setting

	def __parseAttributeStatement(self, statement):
		self.__guardSource(statement)
		patt = r"(?P<attribute_name>\w+) '(?P<attribute_value>[^']+)'"

		match = re.search(patt, statement)
		self.__guardMatch(match, statement)

		attribute_name = match.group('attribute_name')
		attribute_value = match.group('attribute_value')

		setting = AttributeSetting(attribute_name, attribute_value)
		return setting

	def __guardMatch(self, match_object, source):
		if match_object is None:
			msg = 'Recognition exception: {0}'.format(source)
			raise Exception(msg)

	def __guardSource(self, source_text):
		assert source_text is not None and len(source_text) > 0