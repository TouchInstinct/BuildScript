# -*- coding: utf-8 -*-

import os


class BaseBackupCommand:
	def __init__(self, folderPath):
		assert folderPath is not None

		self.folderPath = folderPath

		# вычислять абсолютные пути надо на этапе создания комманды
		# поскольку на этапе выполнения текущая директория может быть удалена
		self.srcAbsPath = self.getAbsSrc()
		self.backupAbsPath = self.getAbsDst()

	def getAbsSrc(self):
		return self.getAbs(self.folderPath)

	def getAbsDst(self):
		absFolderPath = self.getAbs(self.folderPath)
		srcDirName = os.path.basename(absFolderPath)
		absParentDir = os.path.dirname(absFolderPath)
		dstAbs = self.getAbs(os.path.join(absParentDir, 'backup.{0}'.format(srcDirName)))

		return dstAbs

	def getAbs(self, path):
		return os.path.abspath(path)