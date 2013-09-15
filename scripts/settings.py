import patch

build_root = {
	'mdtool' : '/Applications/Xamarin\ Studio.app/Contents/MacOS/mdtool',
	'version' : '0.0.0',
	'parent' : None
}

ios_root = {
	'sln_path' : '/Users/rzaitov/Documents/Apps/BuildScript/BuildSample/BuildSample.sln',
	'parent' : build_root
}

ios_development_root = {
	'files_for_backup' : ['BuildSample.sln', 'BuildSample/CoolApp.csproj'],
	'projects_to_exclude' : ['NotCompileApp'],
	'parent' : ios_root
}

ios_development_production = {
	'name' : 'ios_development_production',
	'sln_config' : 'Release|iPhone',
	'patch' : patch.PathcIos,
	'parent' : ios_development_root
}

ios_development_staging = {
	'name' : 'ios_development_staging',
	'sln_config' : 'Debug|iPhone',
	'patch' : patch.PathcIos,
	'parent' : ios_development_root
}

build_ready_configs = [ios_development_production, ios_development_staging]

