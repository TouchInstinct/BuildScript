import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class CreateBackupCommand(BaseBackupCommand):
	def __init__(self, folderPath):
		BaseBackupCommand.__init__(self, folderPath)

	def execute(self):
		shutil.rmtree(self.backupAbsPath, ignore_errors=True)
		shutil.copytree(self.srcAbsPath, self.backupAbsPath, symlinks=False)