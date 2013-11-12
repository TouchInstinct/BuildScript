import os
import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class RestoreBackupCommand(BaseBackupCommand):
	def __init__(self, folderPath):
		BaseBackupCommand.__init__(self, folderPath)

	def execute(self):
		src = self.getAbsSrc()
		backupDir = self.getAbsDst()

		if os.path.exists(backupDir):
			shutil.rmtree(src, ignore_errors=True)
			shutil.copytree(backupDir, src, symlinks=False)
