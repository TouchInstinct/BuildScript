import os
import shutil

class DeleteBackupCommand:
	def execute(self):
		dirs = [name for name in os.listdir('.') if os.path.isdir(os.path.join('.', name)) & name.startswith('backup.')]
		for dir in dirs:
			shutil.rmtree(dir)