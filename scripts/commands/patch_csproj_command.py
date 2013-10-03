import commands.build_command as bcmd
import utils.csproj.patcher as csproj
import utils.PathConverter.path_converter as path

class PatchCsproj(bcmd.BuildCommand):
	def __init__(self, config):
		bcmd.BuildCommand.__init__(self, config, 'csproj-')
		self._patch_settings = {}

	def ParseConfig(self):
		csproj_keys = self.FetchAllKeysFromConfig()
		self.FillPatchSettings(csproj_keys)


	def FillPatchSettings(self, key_tokens):
		for key_token in key_tokens:
			key_info = self.ParseKeyToken(key_token)

			project_name = key_info[self._group_name]
			key = key_info[self._key_name]
			value = self.ParseValueFromToken(self._config[key_token])

			project_settings = self.FetchSettingForProject(project_name)
			project_settings[key] = value


	def FetchSettingForProject(self, project_name):
		project_settings = self._patch_settings.get(project_name, None)

		if project_settings is None:
			project_settings = {}
			self._patch_settings[project_name] = project_settings

		return project_settings

	def Execute(self):
		converter = path.PathConverter(self._config['sln_path'])

		for project_name in self._patch_settings.keys():
			project_settings = self._patch_settings[project_name]
			self.PatchProject(project_settings, converter)

	def PatchProject(self, project_settings, path_converter):
			csproj_rel_path = project_settings['rel_path']
			csproj_abs_path = path_converter.Convert(csproj_rel_path)

			patcher = csproj.Patcher(csproj_abs_path)
			patcher.AddOrReplace(project_settings, self._config['sln_config'])
