import commands.build_command as bcmd
from parser.CsprojParser.CsprojParser import CsprojParser
import utils.csproj.patcher as csproj

class PatchCsproj(bcmd.BuildCommand):
	def __init__(self, config, path_provider, value_provider):
		assert path_provider is not None
		assert value_provider is not None

		bcmd.BuildCommand.__init__(self, config, 'csproj')
		self._path_provider = path_provider
		self._value_provider = value_provider
		self._parser = None

		self._parseConfig()

	def _parseConfig(self):
		csproj_keys = self.FetchAllKeysFromConfig()
		line_collection = self.__fetchLineCollection(csproj_keys)

		self.__fillPatchSettings(line_collection)

	def __fetchLineCollection(self, keys):
		assert keys is not None

		line_collection = ["{0} '{1}'".format(k, self._config[k]) for k in keys]
		return line_collection

	def __fillPatchSettings(self, line_collection):
		assert line_collection is not None

		self._parser = CsprojParser(line_collection, self._value_provider)
		self._parser.parse()

	def execute(self):
		projects = self._parser.projects_dict.values()

		for project in projects:
			self.__patchProject(project)

	def __patchProject(self, project):
			csproj_abs_path = self._path_provider.resolveAbsPath(project.rel_path)

			patcher = csproj.Patcher(csproj_abs_path)
			patcher.AddOrReplace(project.settings, self._config['sln_config'])