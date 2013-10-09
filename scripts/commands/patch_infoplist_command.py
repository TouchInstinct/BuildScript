from commands.patch_project import PatchProject
from utils.infoplist.patcher import Patcher


class PatchInfoPlist(PatchProject):
	def __init__(self, config, path_provider, value_provider):
		PatchProject.__init__(self, config, path_provider, value_provider, 'plist')

	def _patchProject(self, project):
		abs_path = self._path_provider.resolveAbsPath(project.rel_path)

		patcher = Patcher(abs_path)
		patcher.AddOrReplace(project.settings)
