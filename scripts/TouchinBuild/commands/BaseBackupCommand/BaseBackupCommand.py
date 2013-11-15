# -*- coding: utf-8 -*-
import os
from commands.CommandBase import CommandBase


class BaseBackupCommand(CommandBase):
	def __init__(self, ignoreBackup):
		CommandBase.__init__(self)

		assert ignoreBackup is not None

		self.backupIgnore = ['.git', '.gitignore', '.DS_Store', 'backup']
		self.backupIgnore.extend(ignoreBackup)

		self.folderPath = '.'

		# вычислять абсолютные пути надо на этапе создания комманды
		# поскольку на этапе выполнения текущая директория может быть удалена
		self.srcAbsDirPath = self.getAbsSrc()
		self.backupDirAbsPath = self.getAbsDst()


	def getAbsSrc(self):
		return self.getAbs(self.folderPath)

	def getAbsDst(self):
		absFolderPath = self.getAbs(self.folderPath)

		backupAbsPath = os.path.join(absFolderPath, 'backup')

		return backupAbsPath

	def getAbs(self, path):
		return os.path.abspath(path)