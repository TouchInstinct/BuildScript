import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class CreateBackupCommand(BaseBackupCommand):
	def __init__(self, folderPath):
		BaseBackupCommand.__init__(self, folderPath)

	def execute(self):
		src = self.getAbsSrc()
		backupDir = self.getAbsDst()

		print src, backupDir

		shutil.rmtree(backupDir, ignore_errors=True)
		shutil.copytree(src, backupDir, symlinks=False)