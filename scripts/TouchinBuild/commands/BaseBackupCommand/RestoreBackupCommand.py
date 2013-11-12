import os
import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class RestoreBackupCommand(BaseBackupCommand):
	def __init__(self):
		BaseBackupCommand.__init__(self)

	def execute(self):
		if os.path.exists(self.backupDirAbsPath):
			shutil.rmtree(self.srcAbsDirPath, ignore_errors=True)
			shutil.copytree(self.backupDirAbsPath, self.srcAbsDirPath, symlinks=False)
