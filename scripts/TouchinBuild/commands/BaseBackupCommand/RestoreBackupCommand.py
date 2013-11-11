import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class RestoreBackupCommand(BaseBackupCommand):
	def __init__(self, backupArguments):
		BaseBackupCommand.__init__(self, backupArguments)

	def execute(self):
		src = self.getAbsSrc()
		backupDir = self.getAbsDst()

		shutil.rmtree(src, ignore_errors=True)
		shutil.copytree(backupDir, src, symlinks=False)
