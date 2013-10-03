# -*- coding: utf-8 -*-
import patch

build_root = {
	'mdtool': '/Applications/Xamarin\ Studio.app/Contents/MacOS/mdtool',
	'version': '0.0.0',
	'action': 'build', # 'build'|'setup'|'reset'
	'parent': None
}

ios_root = {
	# relative to script ???
	'sln_path' : '/Users/rzaitov/Documents/Apps/BuildScript/BuildSample/BuildSample.sln',

	# test flight command section
	'tf_publish': True,
	'tf_api_token': '0e6925075d4fc10fed0e7bbf43fa6894_NjQ0OTI2MjAxMi0wOS0yNSAxMTo0MDozNi40OTY5MjU',
	'tf_team_token': 'c5c3cf7a6dae2bea4382dfbd181a2075_Mjc4ODkwMjAxMy0wOS0yOSAxNDowOTo1OC40Mzg5MTY',
	'ft_notes': 'This build was uploaded via the upload API',
	# end section

	'parent' : build_root
}

ios_development_root = {
	# backup command
	'files_for_backup': ['BuildSample.sln', 'BuildSample/CoolApp.csproj', 'BuildSample/Info.plist'],

	# remove_projects
	'projects_to_exclude': ['NotCompileApp'],

	# patch_info_plist
	'plist app:CoolApp rel_path': 'BuildSample/Info.plist',
	'plist app:CoolApp key:CFBundleVersion': '@version',		# set CFBundleVersion
	'plist app:CoolApp key:CFBundleDisplayName': '@app_name',	# set CFBundleDisplayName

	# test flight command section
	'tf_CoolApp_output': 'ipa',

	# patch_csproj
	'csproj group:CoolApp key:rel_path': 'BuildSample/CoolApp.csproj',
	'csproj group:CoolApp key:CodesignProvision': '@codesign_provision',
	'csproj group:CoolApp key:CodesignKey': '@codesign_key',

	'build_steps':[
		# before build
		'std_cmd.py backup',
		'std_cmd.py remove_projects',
		'std_cmd.py copy_provisioning',
		'std_cmd.py patch_info_plist',

		# build
		'std_cmd.py clean',
		'std_cmd.py build'

		# after build
		'std_cmd.py copy_artifacts'
		'std_cmd.py testflight',
	],

	'patch': patch.PathcIos,
	'parent': ios_root
}

ios_development_production = {
	'name': 'ios_development_production',

	# patch_info_plist
	'app_name': 'CoolApp',

	'sln_config': 'Release|iPhone',
	'codesign_key': 'iPhone Developer: Рустам Заитов (CTL85FZX6K)',
	'codesign_provision': '8F606DAE-F9C9-4A19-8EFF-34B990D76C28',

	'parent' : ios_development_root
}

ios_development_staging = {
	'name': 'ios_development_staging',

	# patch_info_plist
	'app_name': 'CoolApp staging',


	'sln_config': 'Debug|iPhone',
	'codesign_key': 'iPhone Developer',
	'codesign_provision': 'F82B1481-F3D0-4CB5-AA6E-8B8D8E3A9DC1',

	'parent': ios_development_root
}

ios_app_store = {
}

# build_ready_configs = [ios_development_production, ios_development_staging]
build_ready_configs = [ios_development_production]
