import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class DeleteBackupCommand(BaseBackupCommand):
	def __init__(self, backupArguments):
		BaseBackupCommand.__init__(self, backupArguments)

	def execute(self):
		shutil.rmtree(self.backupAbsPath, ignore_errors=True)
