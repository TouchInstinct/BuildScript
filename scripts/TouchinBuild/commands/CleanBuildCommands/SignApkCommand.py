from commands.ShellCommandBase import ShellCommandBase


class SignApkCommand(ShellCommandBase):
	def __init__(self, pathToBuildUtil, slnPath, slnConfig, projectName):
		ShellCommandBase.__init__(self)

		assert pathToBuildUtil is not None
		assert slnPath is not None
		assert slnConfig is not None
		assert projectName is not None

		self.pathToBuildUtil = pathToBuildUtil
		self.slnPath = slnPath
		self.slnConfig = slnConfig
		self.projectName = projectName

		self.commandPattern = '{0} -v build "--configuration:{1}" "--project:{2}" /t:SignAndroidPackage "{3}"'

	def execute(self):
		cmdText = self.commandPattern.format(self.pathToBuildUtil, self.slnConfig, self.projectName, self.slnPath)
		print cmdText
		self.executeShell(cmdText)
