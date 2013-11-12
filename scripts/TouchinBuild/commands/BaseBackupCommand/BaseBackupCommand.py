# -*- coding: utf-8 -*-

import os


class BaseBackupCommand:
	def __init__(self):
		self.folderPath = '.'

		# вычислять абсолютные пути надо на этапе создания комманды
		# поскольку на этапе выполнения текущая директория может быть удалена
		self.srcAbsDirPath = self.getAbsSrc()
		self.backupDirAbsPath = self.getAbsDst()

		self.backupIgnore = ['.git', '.gitignore', '.DS_Store']

	def getAbsSrc(self):
		return self.getAbs(self.folderPath)

	def getAbsDst(self):
		absFolderPath = self.getAbs(self.folderPath)
		absParentDir = os.path.dirname(absFolderPath)

		backupAbsPath = os.path.join(absParentDir, 'backup')

		return backupAbsPath

	def getAbs(self, path):
		return os.path.abspath(path)