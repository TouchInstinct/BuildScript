class ValuesStripper:
	def __init__(self):
		pass

	def strip(self, valueStr):
		assert valueStr is not None

		rawValues = valueStr.split(':')
		values = [name.strip() for name in rawValues]

		return values