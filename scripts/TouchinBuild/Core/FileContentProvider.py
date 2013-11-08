class FileContentProvider:
	def __init__(self):
		pass

	def fetchContent(self, path):
		f = open(path)
		content = f.read()

		return content
