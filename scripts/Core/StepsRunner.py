from CommandBuilders.CleanBuildCommandBuilder import CleanBuildCommandBuilder
from CommandBuilders.CopyCommandBuilder import CopyCommandBuilder
from CommandBuilders.CreateBackupCommandBuilder import CreateBackupCommandBuilder
from CommandBuilders.DeleteBackupCommandBuilder import DeleteBackupCommandBuilder
from CommandBuilders.MakeDirsCommandBuilder import MakeDirsCommandBuilder
from CommandBuilders.PatchCsprojCommandBuilder import PatchCsprojCommandBuilder
from CommandBuilders.PatchInfoplistCommandBuilder import PatchInfoplistCommandBuilder
from CommandBuilders.RemoveProjectCommandBuilder import RemoveProjectCommandBuilder
from CommandBuilders.RestoreBackupCommandBuilder import RestoreBackupCommandBuilder
from CommandBuilders.ShCommandBuilder import ShCommandBuilder
from commands.ValueProvider import ValueProvider


class StepsRunner:
	def __init__(self, config, compositeLineProcessor):
		assert config is not None
		assert compositeLineProcessor is not None

		self.lineConveyor = compositeLineProcessor

		self.valueProvider = ValueProvider(config)

		self.shCommandBuilder = ShCommandBuilder()
		self.removeProjectBuilder = RemoveProjectCommandBuilder()
		self.createBackupBuilder = CreateBackupCommandBuilder()
		self.restoreFromBackupBuilder = RestoreBackupCommandBuilder()
		self.deleteBackupBuilder = DeleteBackupCommandBuilder()
		self.createDirs = MakeDirsCommandBuilder()
		self.patchCsproj = PatchCsprojCommandBuilder(config, self.valueProvider)
		self.patchInfoPlist = PatchInfoplistCommandBuilder(self.valueProvider)
		self.copyBuilder = CopyCommandBuilder()

		buildUtilPath = config['build_tool']
		self.cleanBuilder = CleanBuildCommandBuilder(buildUtilPath, 'clean')
		self.buildBuilder = CleanBuildCommandBuilder(buildUtilPath, 'build')

	def run(self, content):
		assert content is not None

		lines = content.splitlines()
		for line in lines:
			processedLine = self.lineConveyor.processLine(line)

			if len(processedLine) == 0:
				continue
			else:
				self.processLine(processedLine)

	def processLine(self, line):
		if self.shCommandBuilder.isShCommand(line):
			cmd = self.shCommandBuilder.getCommandFor(line)
			cmd.execute()
		elif self.removeProjectBuilder.isRemoveProject(line):
			cmd = self.removeProjectBuilder.getCommandFor(line)
			cmd.execute()
		elif self.cleanBuilder.isCleanBuild(line):
			cmd = self.cleanBuilder.getCommandFor(line)
			cmd.execute()
		elif self.buildBuilder.isCleanBuild(line):
			cmd = self.buildBuilder.getCommandFor(line)
			cmd.execute()
		elif self.createBackupBuilder.isCreateBackup(line):
			cmd = self.createBackupBuilder.getCommandFor(line)
			cmd.execute()
		elif self.createDirs.isMakeDirsCommand(line):
			cmd = self.createDirs.getCommandFor(line)
			cmd.execute()
		elif self.patchCsproj.isPatchCsproj(line):
			cmd = self.patchCsproj.getCommandFor(line)
			cmd.execute()
		elif self.patchInfoPlist.isPatchInfoPlist(line):
			cmd = self.patchInfoPlist.getCommandFor(line)
			cmd.execute()
		elif self.copyBuilder.isCopy(line):
			cmd =self.copyBuilder.getCommandFor(line)
			cmd.execute()
		elif self.restoreFromBackupBuilder.isRestoreBackup(line):
			cmd = self.restoreFromBackupBuilder.getCommandFor(line)
			cmd.execute()
		elif self.deleteBackupBuilder.isDeleteBackup(line):
			cmd =self.deleteBackupBuilder.getCommandFor(line)
			cmd.execute()
		else:
			msg = "unrecognised step. Line: '{0}'".format(line)
			raise Exception(msg)