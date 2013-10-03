

class BuildCommand:
	def SetCommandPrefix(self, value):
		self._command_prefix = value
		self._cmd_prefix_len = len(self._command_prefix)

		self._prefix_name= 'prefix'
		self._app_name= 'app'
		self._key_name = 'key'

	def __init__(self, config, cmd_prefix, separator=' '):
		self._separator = separator
		self._config = config
		self.SetCommandPrefix(cmd_prefix)


	def ParseConfig(self):
		return None


	def FetchAllKeysFromConfig(self):
		all_keys = []

		for k in self._config:
			k.startswith(self._command_prefix)
			all_keys.append(k)

		return all_keys


	def ParseKeyToken(self, key_token):
		# csproj-AppName-Key
		identifiers = key_token.split(self._separator)

		result = {
			self._prefix_name: identifiers[0],
			self._app_name: identifiers[1],
			self._key_name: identifiers[2]
		}

		return result


	def ParseValueFromToken(self, value_token):
		value = value_token

		if value_token.startswith('@'):
			key = value_token[1:]
			value = self._config[key]

		return value


	def Execute(self):
		return None
