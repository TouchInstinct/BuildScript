import os
import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class CreateBackupCommand(BaseBackupCommand):
	def __init__(self, ignoreBackup):
		BaseBackupCommand.__init__(self, ignoreBackup)

	def execute(self):
		#if os.path.exists(self.backupDirAbsPath):
		#	raise Exception('folder: {0} already exists'.format(self.backupDirAbsPath))

		dirContent = os.listdir(self.srcAbsDirPath)

		if os.path.exists(self.backupDirAbsPath):
			shutil.rmtree(self.backupDirAbsPath)

		os.mkdir(self.backupDirAbsPath)

		for fileOrDir in dirContent:
			if fileOrDir not in self.backupIgnore:
				self.copyFileOrDirectoryToBackupFolder(fileOrDir)

	def copyFileOrDirectoryToBackupFolder(self, fileOrDirName):
		assert fileOrDirName is not None

		srcAbsPath = os.path.join(self.srcAbsDirPath, fileOrDirName)
		dstAbsPath = os.path.join(self.backupDirAbsPath, fileOrDirName)

		if os.path.isdir(srcAbsPath):
			shutil.copytree(srcAbsPath, dstAbsPath)
		else:
			shutil.copy(srcAbsPath, dstAbsPath)

