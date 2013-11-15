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

		self.commandPattern = '%(mdtool) -v build "--configuration:%(config)" "--project:%(project)" /t:SignAndroidPackage "%(slnPath)"'

	def execute(self):
		cmdText = self.commandPattern % {
		'mdtool': self.pathToBuildUtil,
		'config': self.slnConfig,
		'project': self.projectName,
		'slnPath': self.slnPath
		}

		self.executeShell(cmdText)
