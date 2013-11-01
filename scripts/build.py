import os
import imp
import argparse

import settings
import instruments


keys = instruments.GetConfigKeys(settings.build_ready_configs)

parser = argparse.ArgumentParser()
for key in keys:
	arg = "--{0}".format(key)
	parser.add_argument(arg)

args = parser.parse_args()
cmd_args = vars(args)

# remove unset key-values pairs
for k in cmd_args.keys():
	if cmd_args[k] is None:
		del cmd_args[k]

print cmd_args

build_ready_configs = instruments.GetUnionConfigs(settings.build_ready_configs, cmd_args)

for bc in build_ready_configs:
	print bc['name']

	sln_path = bc['sln_path']
	sln_dir = os.path.dirname(sln_path)

	instruments.CreateOrRestoreFromBackup(sln_dir, bc['files_for_backup'])
	instruments.RemoveProjectFromSolution(sln_path, bc['projects_to_exclude'])

	# try patch source code files
	path_function = bc['patch']
	if path_function is not None:
		path_function(bc)

	if bc['action'] == 'build':
		instruments.CleanSolution(bc['mdtool'], sln_path, bc['sln_config'])
		instruments.BuildSolution(bc['mdtool'], sln_path, bc['sln_config'])

		instruments.CreateOrRestoreFromBackup(sln_dir, bc['files_for_backup'])
		instruments.DeleteBackups(sln_dir, bc['files_for_backup'])

		if 'post_build_file' in bc and 'post_build_actions' in bc:
			path_to_script = bc['post_build_file']
			module_name = os.path.splitext(os.path.basename(path_to_script))[0]
			post_build = imp.load_source(module_name, path_to_script)

			for func_name in bc['post_build_actions']:
				func = getattr(post_build, func_name)
				func(bc)