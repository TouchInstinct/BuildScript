from CommandBuilders.BuilderBackupCommands.CreateBackupCommandBuilder import CreateBackupCommandBuilder
from CommandBuilders.BuilderBackupCommands.DeleteBackupCommandBuilder import DeleteBackupCommandBuilder
from CommandBuilders.BuilderBackupCommands.RestoreBackupCommandBuilder import RestoreBackupCommandBuilder

from CommandBuilders.CleanBuildCommandBuilder import CleanBuildCommandBuilder
from CommandBuilders.CopyCommandBuilder import CopyCommandBuilder
from CommandBuilders.InstallProfileCommandBuilder import InstallProfileCommandBuilder
from CommandBuilders.MakeDirsCommandBuilder import MakeDirsCommandBuilder
from CommandBuilders.PatchCsprojCommandBuilder import PatchCsprojCommandBuilder
from CommandBuilders.PatchInfoPlistArrayCommandBuilder import PatchInfoPlistArrayCommandBuilder
from CommandBuilders.PatchInfoplistCommandBuilder import PatchInfoplistCommandBuilder
from CommandBuilders.PatchManifestCommandBuilder import PatchManifestCommandBuilder
from CommandBuilders.RemoveProjectCommandBuilder import RemoveProjectCommandBuilder
from CommandBuilders.ShCommandBuilder import ShCommandBuilder
from CommandBuilders.SignApkBuilder import SignApkCommandBuilder
from CommandBuilders.TestflightCommandBuilder import TestflightCommandBuilder


class StepsRunner:
	def __init__(self, config, compositeLineProcessor, valueProvider):
		assert config is not None
		assert compositeLineProcessor is not None
		assert valueProvider is not None

		self.lineConveyor = compositeLineProcessor
		self.valueProvider = valueProvider

		self.shCommandBuilder = ShCommandBuilder()
		self.removeProjectBuilder = RemoveProjectCommandBuilder()
		self.createDirs = MakeDirsCommandBuilder()
		self.patchCsproj = PatchCsprojCommandBuilder()
		self.patchInfoPlist = PatchInfoplistCommandBuilder(self.valueProvider)
		self.patchInfoPlistArray = PatchInfoPlistArrayCommandBuilder()
		self.patchManifest = PatchManifestCommandBuilder()
		self.copyBuilder = CopyCommandBuilder()
		self.testflightBuilder = TestflightCommandBuilder()

		ignoreBackup = config.get('ignore_backup', None)
		self.createBackupBuilder = CreateBackupCommandBuilder(ignoreBackup)
		self.restoreFromBackupBuilder = RestoreBackupCommandBuilder(ignoreBackup)
		self.deleteBackupBuilder = DeleteBackupCommandBuilder(ignoreBackup)


		profilePrefix = config['project_name']
		self.installProfileBuilder = InstallProfileCommandBuilder(profilePrefix)

		buildUtilPath = config['build_tool']
		self.cleanBuilder = CleanBuildCommandBuilder(buildUtilPath, 'clean')
		self.buildBuilder = CleanBuildCommandBuilder(buildUtilPath, 'build')
		self.signAndroid = SignApkCommandBuilder(buildUtilPath)

	def run(self, content):
		assert content is not None

		lines = content.splitlines()
		for line in lines:
			processedLine = self.lineConveyor.processText(line, self.lineConveyor)

			if len(processedLine) == 0:
				continue
			else:
				self.processLine(processedLine)

	def processLine(self, line):
		if self.shCommandBuilder.isShCommand(line):
			cmd = self.shCommandBuilder.getCommandFor(line)
		elif self.removeProjectBuilder.isRemoveProject(line):
			cmd = self.removeProjectBuilder.getCommandFor(line)
		elif self.cleanBuilder.isCleanBuild(line):
			cmd = self.cleanBuilder.getCommandFor(line)
		elif self.buildBuilder.isCleanBuild(line):
			cmd = self.buildBuilder.getCommandFor(line)
		elif self.signAndroid.isSignApk(line):
			cmd = self.signAndroid.getCommandFor(line)
		elif self.createBackupBuilder.isCreateBackup(line):
			cmd = self.createBackupBuilder.getCommandFor(line)
		elif self.createDirs.isMakeDirsCommand(line):
			cmd = self.createDirs.getCommandFor(line)
		elif self.patchCsproj.isPatchCsproj(line):
			cmd = self.patchCsproj.getCommandFor(line)
		elif self.patchInfoPlist.isPatchInfoPlist(line):
			cmd = self.patchInfoPlist.getCommandFor(line)
		elif self.patchInfoPlistArray.isPatchInfoPlist(line):
			cmd = self.patchInfoPlistArray.getCommandFor(line)
		elif self.patchManifest.isManifestCommand(line):
			cmd = self.patchManifest.getCommandFor(line)
		elif self.copyBuilder.isCopy(line):
			cmd =self.copyBuilder.getCommandFor(line)
		elif self.restoreFromBackupBuilder.isRestoreBackup(line):
			cmd = self.restoreFromBackupBuilder.getCommandFor(line)
		elif self.deleteBackupBuilder.isDeleteBackup(line):
			cmd =self.deleteBackupBuilder.getCommandFor(line)
		elif self.testflightBuilder.isTestflight(line):
			cmd = self.testflightBuilder.getCommandFor(line)
		elif self.installProfileBuilder.isInstallProfile(line):
			cmd = self.installProfileBuilder.getCommandFor(line)
		else:
			msg = "unrecognised step. Line: '{0}'".format(line)
			raise Exception(msg)

		print 'start: {0}'.format(line)
		cmd.execute()
		print 'finish: {0}'.format(line)
