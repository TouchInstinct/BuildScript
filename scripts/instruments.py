import shutil
import os

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