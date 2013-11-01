import os
import shutil


class RestoreBackupCommand:
	def execute(self):
		dirPairs = [(name, "backup.{0}".format(name)) for name in os.listdir('.') if os.path.isdir(name) and not name.startswith('backup.')]

		for pair in dirPairs:
			absPair = (pair[0], pair[1])
			if not os.path.exists(absPair[1]):
				continue

			shutil.rmtree(absPair[0])				# delete src
			shutil.copytree(absPair[1], absPair[0])	# restore from backup
