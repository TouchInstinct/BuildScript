import os


class BaseBackupCommand:
	def __init__(self, folderPath):
		assert folderPath is not None

		self.folderPath = folderPath

	def getAbsSrc(self):
		return self.getAbs(self.folderPath)

	def getAbsDst(self):
		srcDirName = os.path.dirname(self.folderPath)
		return self.getAbs('backup'.format(srcDirName))

	def getAbs(self, path):
		return os.path.abspath(path)