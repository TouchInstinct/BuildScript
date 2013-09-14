import shutil
import os

def CreateOrRestoreFromBackup(base_dir, relative_path_to_files):
	
	for rel_path in relative_path_to_files:

		abs_path = os.path.join(base_dir, rel_path)
		abs_path_backup = "{0}.build_backup".format(os.path)
		
		if os.path.exists(abs_path_backup):
			# restore from backup
			shutil.copyfile(abs_path_backup, abs_path)
		else:
			# create backup
			shutil.copyfile(abs_path, abs_path_backup)

	return None
