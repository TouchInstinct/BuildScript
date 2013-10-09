from commands.ValueProvider import ValueProvider
import commands.patch_infoplist_command as plist
import path_provider

config = {
	'version': '0.1.2',
	'app_name': 'TestAppName',

	# patch_info_plist
	'plist app:CoolApp rel_path': 'BuildSample/Info.plist',
	'plist app:CoolApp key:CFBundleVersion': '@version',		# set CFBundleVersion
	'plist app:CoolApp key:CFBundleDisplayName': '@app_name',	# set CFBundleDisplayName
}

base_dir = '/Users/rzaitov/Documents/Apps/BuildScript/BuildSample'
provider = path_provider.PathProvider(base_dir)
value_provider = ValueProvider(config)

command = plist.PatchInfoPlist(config, provider, value_provider)
command.execute()
