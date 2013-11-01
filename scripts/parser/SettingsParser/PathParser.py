class PathParser:
	def __init__(self):
		pass

	def parse(self, line):
		assert line is not None

		pathSegments = line.split('.')
		self._guardPathSegments(pathSegments, line)

		return pathSegments

	def _guardPathSegments(self, pathSegments, sourceLine):
		if '' in pathSegments:
			raise Exception('invalid path given: {0}'.format(sourceLine))


