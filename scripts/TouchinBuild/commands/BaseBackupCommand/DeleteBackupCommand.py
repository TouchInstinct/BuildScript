import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class DeleteBackupCommand(BaseBackupCommand):
	def __init__(self):
		BaseBackupCommand.__init__(self)

	def execute(self):
		shutil.rmtree(self.backupDirAbsPath, ignore_errors=True)
