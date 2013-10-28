import os
import shutil

class DeleteBackupCommand:
	def __init__(self, pathProvider):
		assert pathProvider is not None

		self.__pathProvider = pathProvider

	def execute(self):
		baseDir = self.__pathProvider.resolveAbsPath('.')

		dirs = [self.__pathProvider.resolveAbsPath(name) for name in os.listdir(baseDir) if os.path.isdir(os.path.join(baseDir, name)) & name.startswith('backup.')]
		for dir in dirs:
			shutil.rmtree(dir)