import os
import shutil

class DeleteBackupCommand:
	def __init__(self):
		pass

	def execute(self):
		dirs = [name for name in os.listdir('.') if os.path.isdir(os.path.join('.', name)) & name.startswith('backup.')]
		for d in dirs:
			shutil.rmtree(d)