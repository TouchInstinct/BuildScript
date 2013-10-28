import os
import shutil


class RestoreBackupCommand:
	def __init__(self, pathProvider):
		assert pathProvider is not None

		self.__pathProvider = pathProvider

	def execute(self):
		baseDir = self.__pathProvider.resolveAbsPath('.')

		dirPairs = [(name, "backup.{0}".format(name)) for name in os.listdir(baseDir) if os.path.isdir(self.__pathProvider.resolveAbsPath(name)) and not name.startswith('backup.')]

		for pair in dirPairs:
			if not os.path.exists(pair[1]):
				continue

			shutil.rmtree(pair[0])				# delete src
			shutil.copytree(pair[1], pair[0])	# restore from backup
