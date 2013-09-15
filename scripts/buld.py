import os

import settings
import instruments

cmd_args = {'version' : '1.2.3', 'some_field' : 'some_value', 'action' : 'setup'}

instruments.CompileConfigs(settings.build_ready_configs, cmd_args)

for bc in settings.build_ready_configs:
	sln_path = bc['sln_path']
	sln_dir = os.path.dirname(sln_path)

	instruments.CreateOrRestoreFromBackup(sln_dir, bc['files_for_backup'])
	instruments.RemoveProjectFromSolution(sln_path, bc['projects_to_exclude'])

	# try patch source code files
	path_function = bc['patch']
	if path_function is not None:
		path_function(bc)

	if bc['action'] == 'build':
		instruments.CleanSolution(bc['mdtool'], sln_path)
		instruments.BuildSolution(bc['mdtool'], sln_path, bc['sln_config'])

		instruments.CreateOrRestoreFromBackup(sln_dir, settings.files_for_backup)
		instruments.DeleteBackups(sln_dir, settings.files_for_backup)