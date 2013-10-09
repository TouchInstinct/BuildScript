import commands.build_command as bcmd
from parser.ProjectParser.ProjectParser import ProjectParser


class PatchProject(bcmd.BuildCommand):
	def __init__(self, config, path_provider, value_provider, command_token):
		assert path_provider is not None
		assert value_provider is not None
		assert command_token is not None

		bcmd.BuildCommand.__init__(self, config, command_token)
		self._path_provider = path_provider
		self._value_provider = value_provider
		self._command_token = command_token

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

		self._parser = ProjectParser(line_collection, self._value_provider, self._command_token)
		self._parser.parse()

	def execute(self):
		projects = self._parser.projects_dict.values()

		for project in projects:
			self._patchProject(project)

	def _patchProject(self, project):
		print 'Do nothing'
		# override this method to do useful work
		pass
