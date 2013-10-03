from parser.StringValueParser import *
from parser.AttributeNameParser import *

class CsprojParser:
	def __init__(self, string_to_parse, value_token, config):
		self._config = config
		self._token_buffer = string_to_parse.split(' ')
		self._token_buffer.append(value_token)
		self._token_index = 0;
		self._project = None

	def Parse(self):
		while self._token_index < len(self._token_buffer):
			self.ProcessToken()


	def ProcessToken(self):
		token = self.getCurrentToken()

		if self.isCsprojStatement(token):
			self._token_index += 1
		elif self.isAppToken(token):
			self.processAppToken(token)
			self._token_index += 1
		elif self.isAttributeToken(token):
			attribute_name = self.processAttributeNameToken(token)
			self._token_index += 1
			token = self.getCurrentToken()
			attribute_value = self.processAttributeValueToken(token)
			setattr(self.project, attribute_name, attribute_value)

	def isCsprojStatement(self, token):
		return token == 'csproj'

	def isAppToken(self, token):
		return token.startswith('app:')

	def isAttributeToken(self, token):
		return ':' not in token

	def processAppToken(self, appToken):
		appName = appToken[len('app:')]

		self.project = Csproj(appName)
		self._settings[appName] = self.project

	def processAttributeNameToken(self, token):
		attribute_name = token
		return attribute_name

	def processAttributeValueToken(self, token):
		value = token

		if token.startswith('@'):
			key = token[1:]
			value = self._config[key]

		return value

	def getCurrentToken(self):
		token = self._token_buffer[self._token_index]
		return token

class Csproj:
	def __init__(self, appName):
		self.appName = appName