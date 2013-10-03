import commands.patch_infoplist_command as plist
import os

config = {
	'version': '0.1.2',

	# patch_info_plist
	'plist-CoolApp_rel_path': 'BuildSample/Info.plist',
	'plist-CoolApp_CFBundleVersion': '@version',		# set CFBundleVersion
	'plist-CoolApp_CFBundleDisplayName': '@app_name',	# set CFBundleDisplayName

}

base_dir = '/Users/rzaitov/Documents/Apps/BuildScript',

class PathProvider:
	def __init__(self, base_dir):
		self._base_dir = base_dir

	def ResolveAbsPath(self, rel_path):
		abs_path = os.path.join(self._base_dir, rel_path)
		return abs_path

provider = PathProvider(base_dir)
patcher = plist.PatchInfoPlist(config, provider)
patcher.Execute()
