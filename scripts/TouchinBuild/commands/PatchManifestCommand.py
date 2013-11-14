from commands.CommandBase import CommandBase
from utils.ManifestPatcher import ManifestPatcher


class PatchManifestCommand(CommandBase):
	def __init__(self, pathToManifest, key, value):
		CommandBase.__init__(self)

		assert pathToManifest is not None
		assert key is not None
		assert value is not None

		self.pathToManifest = pathToManifest
		self.key = key
		self.value = value

	def execute(self):
		patcher = ManifestPatcher(self.pathToManifest)

		patcher.AddOrReplaceManifestAtr(self.key, self.value)
