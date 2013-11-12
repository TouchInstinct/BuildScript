import os
import shutil
from commands.BaseBackupCommand.BaseBackupCommand import BaseBackupCommand


class RestoreBackupCommand(BaseBackupCommand):
	def __init__(self):
		BaseBackupCommand.__init__(self)

	def execute(self):
		if not os.path.exists(self.backupDirAbsPath):
			raise Exception('backup folder: {0} not exists'.format(self.backupDirAbsPath))

		srcDirContent = os.listdir(self.srcAbsDirPath)
		for fileOrDir in srcDirContent:
			if fileOrDir not in self.backupIgnore:
				self.removeFileOrDirectory(fileOrDir)

		backupDirContent = os.listdir(self.backupDirAbsPath)
		for fileOrDir in backupDirContent:
			self.copyFileOrDirectoryFromBackupFolder(fileOrDir)

	def removeFileOrDirectory(self, fileOrDirName):

		srcAbsPath = os.path.join(self.srcAbsDirPath, fileOrDirName)

		if os.path.isdir(srcAbsPath):
			shutil.rmtree(srcAbsPath)
		else:
			os.remove(srcAbsPath)

	def copyFileOrDirectoryFromBackupFolder(self, fileOrDirName):
		assert fileOrDirName is not None

		srcAbsPath = os.path.join(self.srcAbsDirPath, fileOrDirName)
		fileInBackupFolderAbsPath = os.path.join(self.backupDirAbsPath, fileOrDirName)

		if os.path.isdir(fileInBackupFolderAbsPath):
			shutil.copytree(fileInBackupFolderAbsPath, srcAbsPath)
		else:
			shutil.copy(fileInBackupFolderAbsPath, srcAbsPath)
