import os


class BaseBackupCommand:
	def __init__(self, backupArguments):
		assert backupArguments is not None

		self.backupArguments = backupArguments

	def getAbsSrc(self):
		return self.getAbs(self.backupArguments.getSourceFolderName())

	def getAbsDst(self):
		return self.getAbs(self.backupArguments.getBackupFolderName())

	def getAbs(self, path):
		return os.path.abspath(path)