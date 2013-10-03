class StringValueParser:
	def __init__(self, valid_string, model):
		self._valid_string = valid_string
		self._model = model

	def IsTokenValid(self, token):
		return token == self._valid_string

	def ProcessToken(self, token):
		pass
