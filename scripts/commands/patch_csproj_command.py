import commands.build_command as bcmd
import utils.csproj.patcher as csproj
import parser.CsprojParser as parser

class PatchCsproj(bcmd.BuildCommand):
	def __init__(self, config, path_provider):
		bcmd.BuildCommand.__init__(self, config, 'csproj')
		self._path_provider = path_provider
		self._parser = None

	def ParseConfig(self):
		csproj_keys = self.FetchAllKeysFromConfig()
		self.FillPatchSettings(csproj_keys)


	def FillPatchSettings(self, key_tokens):
		self._parser = parser.CsprojParser(self._config)

		for key_token in key_tokens:
			self._parser.parse(key_token, self._config[key_token])


	def Execute(self):
		projects_list = self._parser.projects

		for project in projects_list:
			self.PatchProject(project)

	def PatchProject(self, project):
			csproj_abs_path = self._path_provider.fetchAbsPath(project.rel_path)

			patcher = csproj.Patcher(csproj_abs_path)
			patcher.AddOrReplace(project.settings, self._config['sln_config'])
