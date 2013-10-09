from commands.patch_project import PatchProject
import utils.csproj.patcher as csproj

class PatchCsproj(PatchProject):
	def __init__(self, config, path_provider, value_provider):
		PatchProject.__init__(self, config, path_provider, value_provider, 'csproj')

	def _patchProject(self, project):
		csproj_abs_path = self._path_provider.resolveAbsPath(project.rel_path)

		patcher = csproj.Patcher(csproj_abs_path)
		patcher.AddOrReplace(project.settings, self._config['sln_config'])