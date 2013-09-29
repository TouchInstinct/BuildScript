# -*- coding: utf-8 -*-
import patch

build_root = {
	'mdtool': '/Applications/Xamarin\ Studio.app/Contents/MacOS/mdtool',
	'version': '0.0.0',
	'action': 'build', # 'build'|'setup'
	'parent': None
}

ios_root = {
	'sln_path' : '/Users/rzaitov/Documents/Apps/BuildScript/BuildSample/BuildSample.sln',
	'parent' : build_root
}

ios_development_root = {
	'files_for_backup': ['BuildSample.sln', 'BuildSample/CoolApp.csproj', 'BuildSample/Info.plist'],
	'projects_to_exclude': ['NotCompileApp'],
	'info_plist_rel_path': 'BuildSample/Info.plist',

	'post_build_file': 'post_build.py',
	'post_build_actions' : ['PublishToTestFlight', 'PrintToConsole'],

	'patch': patch.PathcIos,
	'parent': ios_root
}

ios_development_production = {
	'name': 'ios_development_production',

	'sln_config': 'Release|iPhone',
	'codesign_key': 'iPhone Developer: Рустам Заитов (CTL85FZX6K)',
	'codesign_provision': '8F606DAE-F9C9-4A19-8EFF-34B990D76C28',

	'parent' : ios_development_root
}

ios_development_staging = {
	'name': 'ios_development_staging',

	'sln_config': 'Debug|iPhone',
	'codesign_key': 'iPhone Developer',
	'codesign_provision': 'F82B1481-F3D0-4CB5-AA6E-8B8D8E3A9DC1',

	'parent': ios_development_root
}

ios_app_store = {
}

# build_ready_configs = [ios_development_production, ios_development_staging]
build_ready_configs = [ios_development_production]
