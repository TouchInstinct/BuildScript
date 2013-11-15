class ValuesStripper:
	def __init__(self, separator=':'):
		assert separator is not None

		self.separator = separator

	def strip(self, valueStr):
		assert valueStr is not None

		rawValues = valueStr.split(self.separator)
		values = [name.strip() for name in rawValues]

		return values