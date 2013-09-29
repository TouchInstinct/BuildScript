import os

import settings
import instruments
import argparse

cmd_args = {'version' : '1.2.3', 'some_field' : 'some_value', 'action' : 'build'}
keys = instruments.GetConfigKeys(settings.build_ready_configs)

parser = argparse.ArgumentParser()
for key in keys:
	arg = "--{0}".format(key)
	parser.add_argument(arg)

args = parser.parse_args()
print vars(args)

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