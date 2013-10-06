from parser.StringValueParser import *
from parser.AttributeNameParser import *
from parser.token import Token


class CsprojParser:
	def __init__(self, config):
		self._config = config
		self._statement_buffer = None
		self._token_index = 0
		self._current_project = None
		self._projects = {}

	def getProjects(self):
		return self._projects.values()

	def initStatementBuffer(self, string_to_parse, value_statement):
		self._statement_buffer = string_to_parse.split(' ')
		self._statement_buffer.append(value_statement)
		self._token_index = 0

	def parse(self, string_to_parse, value_token):
		self.initStatementBuffer(string_to_parse, value_token)

		while self._token_index < len(self._statement_buffer):
			self.ProcessStatement()


	def ProcessStatement(self):
		text = self.getCurrentStatement()

		if self.isCsprojStatement(text):
			self.procCspojStatement(text)

		elif self.isAppStatement(text):
			self.procAppStatement(text)

		elif self.isKeyStatement(text):
			self.procKeyStatement(text)

		elif self.isAttributeToken(text):
			self.procAttributeToken(text)

		else:
			raise Exception('unrecognized token', text)

	def isCsprojStatement(self, text):
		return text == 'csproj'

	def procCspojStatement(self, text):
		self._token_index += 1

	def isAppStatement(self, token):
		return token.startswith('app:')

	def procAppStatement(self, text):
		self.processAppToken(text)
		self._token_index += 1

	def isKeyStatement(self, text):
		return text.startswith('key:')

	def procKeyStatement(self, text):
		key_token = self.parseKeyToken(text)

		self._token_index += 1
		text = self.getCurrentStatement()
		value_token = self.parseValueToken(text)
		value = self.fetchValueFromValueToken(value_token)

		self._current_project.settings[key_token.content] = value
		self._token_index += 1

	def isAttributeToken(self, token):
		return ':' not in token

	def procAttributeToken(self, text):
		attribute_token = self.parseValueToken(text)

		self._token_index += 1
		text = self.getCurrentStatement()
		value_token = self.parseValueToken(text)
		setattr(self._current_project, attribute_token.content, value_token.content)

		self._token_index += 1

	def parseAppToken(self, text):
		appName = text[len('app:'):]
		token = Token(appName, 'appToken')

		return token

	def processAppToken(self, text):
		appToken = self.parseAppToken(text)
		self.setCurrentProject(appToken.content)

	def setCurrentProject(self, appName):
		exists = appName in self._projects

		self._current_project = self._projects[appName] if exists else Csproj(appName)
		self._projects[appName] = self._current_project

	def parseKeyToken(self, text):
		key_name = text[len('key:'):]
		token = Token(key_name, 'keyToken')

		return token

	def parseValueToken(self, text):
		token = Token(text, 'valueToken')

		return token

	def fetchValueFromValueToken(self, token):
		value = token.content

		if value.startswith('@'):
			key = value[1:]
			value = self._config[key]

		return value

	def getCurrentStatement(self):
		token = self._statement_buffer[self._token_index]
		return token


class Csproj:
	def __init__(self, appName):
		self.appName = appName
		self.settings = {}

	def __str__(self):
		return 'app Name: {0} settings: {1}'.format(self.appName, self.settings)