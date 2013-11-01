import shutil

class CreateBackupCommand:
	def __init__(self, backupArguments):
		assert backupArguments is not None

		self.__backupArguments = backupArguments

	def execute(self):
		src = self.__backupArguments.getSourceFolderName()
		dst = self.__backupArguments.getBackupFolderName()

		shutil.rmtree(dst, ignore_errors=True)
		shutil.copytree(src, dst, symlinks=False)
