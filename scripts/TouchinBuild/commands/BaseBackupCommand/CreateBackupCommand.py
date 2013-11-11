import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class CreateBackupCommand(BaseBackupCommand):
	def __init__(self, backupArguments):
		BaseBackupCommand.__init__(self, backupArguments)

	def execute(self):
		src = self.getAbsSrc()
		backupDir = self.getAbsDst()

		shutil.rmtree(backupDir, ignore_errors=True)
		shutil.copytree(src, backupDir, symlinks=False)
