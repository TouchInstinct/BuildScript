class CreateBackupArguments:
	def __init__(self):
		self.folderName = None

	def getSourceFolderName(self):
		return self.folderName

	def getBackupFolderName(self):
		return "backup.{0}".format(self.folderName)


