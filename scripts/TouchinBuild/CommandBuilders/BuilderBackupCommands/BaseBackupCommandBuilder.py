from parsers.ValuesStriper import ValuesStripper


class BaseBackupCommandBuilder:
	def __init__(self, ignoreBackupStr):

		if ignoreBackupStr:
			splitter = ValuesStripper(',')
			values = splitter.strip(ignoreBackupStr)
			self.ignoreBackup = values
		else:
			self.ignoreBackup = []