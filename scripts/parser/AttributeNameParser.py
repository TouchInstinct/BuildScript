import parser.StringValueParser as parser

class AttributeNameParser(parser.StringValueParser):
	def __init__(self, attribute_name, model):
		parser.StringValueParser.__init__(self, attribute_name, model)

	def ProcessToken(self, token):
		self._model.rel_path = ''
