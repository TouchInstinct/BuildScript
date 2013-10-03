from parser.StringValueParser import *
from parser.AttributeNameParser import *

class CsprojParser:
	def __init__(self, config):
		self._config = config
		self._token_buffer = None
		self._token_index = 0
		self._current_project = None
		self.projects = {}

	def initTokenBuffer(self, string_to_parse, value_token):
		self._token_buffer = string_to_parse.split(' ')
		self._token_buffer.append(value_token)
		self._token_index = 0


	def parse(self, string_to_parse, value_token):
		self.initTokenBuffer(string_to_parse, value_token)

		while self._token_index < len(self._token_buffer):
			self.ProcessToken()


	def ProcessToken(self):
		token = self.getCurrentToken()

		if self.isCsprojStatement(token):
			self._token_index += 1
		elif self.isAppToken(token):
			self.processAppToken(token)
			self._token_index += 1
		elif self.isKeyToken(token):
			key_name = self.processKeyToken(token)
			self._token_index += 1
			token = self.getCurrentToken()
			value = self.processValueToken()
			self._token_index += 1
			self._current_project.settings[key_name] = value
		elif self.isAttributeToken(token):
			attribute_name = self.processAttributeNameToken(token)
			self._token_index += 1
			token = self.getCurrentToken()
			attribute_value = self.processValueToken(token)
			self._token_index += 1
			setattr(self.project, attribute_name, attribute_value)

	def isCsprojStatement(self, token):
		return token == 'csproj'

	def isAppToken(self, token):
		return token.startswith('app:')

	def isKeyToken(self, token):
		return token.startswith('key:')

	def isAttributeToken(self, token):
		return ':' not in token

	def processAppToken(self, appToken):
		appName = appToken[len('app:')]
		self.setCurrentProject(appName)

	def setCurrentProject(self, appName):
		exists = appName in self.projects

		self._current_project = self.projects[appName] if exists else Csproj(appName)
		self.projects[appName] = self._current_project

	def processKeyToken(self, token):
		key_name = token[len('key:')]
		return key_name

	def processAttributeNameToken(self, token):
		attribute_name = token
		return attribute_name

	def processValueToken(self, token):
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
		self.settings = {}