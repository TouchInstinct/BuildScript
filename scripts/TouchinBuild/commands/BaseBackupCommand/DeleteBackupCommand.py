import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class DeleteBackupCommand(BaseBackupCommand):
	def __init__(self, backupArguments):
		BaseBackupCommand.__init__(self, backupArguments)

	def execute(self):
		backupDir = self.getAbsDst()

		shutil.rmtree(backupDir, ignore_errors=True)
