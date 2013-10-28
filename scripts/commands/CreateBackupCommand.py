import shutil

class CreateBackupCommand:
	def __init__(self, pathProvider, createBackupArguments):
		assert pathProvider is not None
		assert createBackupArguments is not None

		self.__pathProvider = pathProvider
		self.__createBackupArguments = createBackupArguments

	def execute(self):
		src = self.__pathProvider.resolveAbsPath(self.__createBackupArguments.getSourceFolderName())
		dst = self.__pathProvider.resolveAbsPath(self.__createBackupArguments.getBackupFolderName())

		shutil.rmtree(dst, ignore_errors=True)
		shutil.copytree(src, dst, symlinks=False)
