from Core.ContentProviderBase import ContentProviderBase


class FileContentProvider(ContentProviderBase):
	def __init__(self):
		ContentProviderBase.__init__(self)

	def fetchContent(self, path):
		f = open(path)
		content = f.read()

		return content
