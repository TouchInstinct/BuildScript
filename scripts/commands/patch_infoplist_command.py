import commands.build_command as bcmd
import utils.PathConverter.path_converter as pc
import utils.infoplist.patcher as plist


class PatchInfoPlist(bcmd.BuildCommand):
	def __init__(self, config, path_provider):
		bcmd.BuildCommand.__init__(self, config, 'plist')
		self._info_plist_rel_path = None
		self._path_provider = path_provider
		self._plist_dict = {}

		self.ParseConfig()

	def ParseConfig(self):
		self.FetchInfoPlistPath()
		self.FetchAllParams()

	def FetchInfoPlistPath(self):
		self._info_plist_rel_path = self._config['info_plist_rel_path']

	def FetchAllParams(self):
		all_conf_keys = self.FetchAllConfigKeys()

		for k in all_conf_keys:
			self.AddValueFor(k)

	def FetchAllConfigKeys(self):
		all_keys = []
		for k in self._config.keys():
			if k.startswith(PatchInfoPlist._command_prefix) and not k.endswith('rel_path'):
				all_keys.append(k)

		return all_keys

	def AddValueFor(self, conf_key):
		value_token = self._config[conf_key]
		value = self.ParseValueFromToken(value_token)

		k = self.ParsePlistKeyFrom(conf_key)
		self._plist_dict[k] = value


	def ParsePlistKeyFrom(self, config_key):
		return config_key[PatchInfoPlist._cmd_prefix_len:]

	def Execute(self):
		info_plist_abs_path = self._path_provider.ResolveAbsPath(self._info_plist_rel_path)
		patcher = plist.Patcher(info_plist_abs_path)

		patcher.AddOrReplace(self._plist_dict)
