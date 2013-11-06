class FileContentProvider:
	def __init__(self):
		pass

	def fetchContent(self, path):
		file = open(path)
		content = file.read()

		return content
