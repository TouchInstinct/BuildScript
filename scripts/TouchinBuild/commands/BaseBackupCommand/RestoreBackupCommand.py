import os
import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class RestoreBackupCommand(BaseBackupCommand):
	def __init__(self, folderPath):
		BaseBackupCommand.__init__(self, folderPath)

	def execute(self):
		if os.path.exists(self.backupAbsPath):
			shutil.rmtree(self.srcAbsPath, ignore_errors=True)
			shutil.copytree(self.backupAbsPath, self.srcAbsPath, symlinks=False)
