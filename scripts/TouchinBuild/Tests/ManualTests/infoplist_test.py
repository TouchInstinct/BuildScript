from CommandBuilders.PatchInfoplistCommandBuilder import PatchInfoplistCommandBuilder
from commands.ValueProvider import ValueProvider

config = {
	'version': '0.1.2',
	'app_name': 'TestAppName',

	# patch_info_plist
	'plist app:CoolApp rel_path': 'BuildSample/Info.plist',
	'plist app:CoolApp key:CFBundleVersion': '@version',		# set CFBundleVersion
	'plist app:CoolApp key:CFBundleDisplayName': '@app_name',	# set CFBundleDisplayName
}
line = "inside 'BuildSample/BuildSample/Info.plist' set CFBundleDisplayName to 'MyCoolApp'"

value_provider = ValueProvider(config)
builder = PatchInfoplistCommandBuilder(value_provider)

command = builder.getCommandFor(line)
command.execute()
