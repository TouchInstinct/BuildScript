class BackupArguments:
	def __init__(self):
		self.folderPath = None

	def getSourceFolderName(self):
		return self.folderPath

	def getBackupFolderName(self):
		return "backup.{0}".format(self.folderPath)


