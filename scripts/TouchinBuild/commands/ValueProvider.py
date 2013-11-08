class ValueProvider:
	def __init__(self):
		self.__config = None

	def setConfig(self, config):
		assert config is not None
		self.__config = config

	def getValueFor(self, link):
		is_link = link.startswith('@')
		result = link

		if is_link:
			key = link[1:]
			result = self.__config[key]

		return result