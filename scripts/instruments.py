from subprocess import call
import shutil
import os
import re

def MapToBackupName(origin_path):

	backup_path = "{0}.build_backup".format(origin_path)
	return backup_path

def FetchAbsOriginBackupInfo(base_dir, rel_path_to_origin_files):

	abs_path_to_origin_files = [os.path.join(base_dir, rel) for rel in rel_path_to_origin_files]
	abs_origin_backup_infos = [{'origin': p, 'backup': MapToBackupName(p)} for p in abs_path_to_origin_files]
	
	return abs_origin_backup_infos

def CreateOrRestoreFromBackup(base_dir, relative_path_to_files):

	abs_origin_backup_infos = FetchAbsOriginBackupInfo(base_dir, relative_path_to_files)

	for aobi in abs_origin_backup_infos:

		abs_original = aobi['origin']
		abs_backup = aobi['backup']

		if os.path.exists(abs_backup):
			# restore from backup
			shutil.copyfile(abs_backup, abs_original)
		else:
			# create backup
			shutil.copyfile(abs_original, abs_backup)

	return None

def DeleteBackups(base_dir, relative_path_to_files):

	abs_origin_backup_infos = FetchAbsOriginBackupInfo(base_dir, relative_path_to_files)

	for aobi in abs_origin_backup_infos:

		abs_backup = aobi['backup']

		if os.path.exists(abs_backup):
			os.remove(abs_backup)

	return None

def ResetDirectory(base_dir, relative_path_to_files):

	CreateOrRestoreFromBackup(base_dir, relative_path_to_files)
	DeleteBackups(base_dir, relative_path_to_files)

	return None

def RemoveProjectFromSolution(abs_path_to_sln, project_names):

	sln_file = open(abs_path_to_sln, 'r+')
	content = sln_file.read()

	for pn in project_names:
		reg_pattern = r'\n*Project.*?"{0}".*?\n*EndProject'.format(pn)
		content = re.sub(reg_pattern, "", content)

	# override file
	sln_file.seek(0)
	sln_file.write(content)
	sln_file.truncate()
	sln_file.close()

def CleanSolution(mdtool, abs_path_to_sln, config):

	clean_cmd_pattern = '{0} -v build "--configuration:{1}" "--target:Clean" {2}'
	clean_cmd_text = clean_cmd_pattern.format(mdtool, config, abs_path_to_sln)

	print(clean_cmd_text)
	ret_code = call(clean_cmd_text, shell=True)
	print('finished with return code: {0}'.format(ret_code))

def BuildSolution(mdtool, abs_path_to_sln, config):

	build_cmd_pattern = '{0} -v build "--configuration:{1}" "--target:Build" {2}'
	build_cmd_text = build_cmd_pattern.format(mdtool, config, abs_path_to_sln)

	print(build_cmd_text)
	ret_code = call(build_cmd_text, shell=True)
	print('finished with return code: {0}'.format(ret_code))

def GetUnionConfigs(configs_lst, cmd_args=None):

	union_configs = []
	for c_dict in configs_lst:

		ancestors = GetAncestorsFromRootTo(c_dict)
		if cmd_args is not None:
			ancestors.append(cmd_args)

		union_config = {}
		for a in ancestors:
			union_config.update(a)

		union_configs.append(union_config)

	return union_configs

def GetConfigKeys(configs_lst):
	union_configs = GetUnionConfigs(configs_lst)

	keys = [];
	for config in union_configs:
		for key in config.keys():
			keys.append(key)

	# remove duplicates
	keys = list(set(keys))

	return keys

def GetAncestorsFromRootTo(config):

	ancestors = []
	c = config

	while c is not None:
		ancestors.append(c)
		c = c['parent']

	ancestors.reverse()
	return ancestors