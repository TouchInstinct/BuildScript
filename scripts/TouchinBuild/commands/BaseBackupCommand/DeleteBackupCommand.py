import os
import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class DeleteBackupCommand(BaseBackupCommand):
	def __init__(self, ignoreBackup):
		BaseBackupCommand.__init__(self, ignoreBackup)

	def execute(self):
		if not os.path.exists(self.backupDirAbsPath):
			raise Exception('backup folder: {0} not exists'.format(self.backupDirAbsPath))

		shutil.rmtree(self.backupDirAbsPath, ignore_errors=True)
