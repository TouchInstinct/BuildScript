import os

import settings
import instruments

# print("all projects:")
# print(settings.all_projects)

# project_to_remove = settings.projects_to_exclude[0];
# print("project to remove:")
# print(project_to_remove);


# projects_to_build = settings.all_projects[:]
# projects_to_build.remove(project_to_remove)

# print("projects to build:")
# print(projects_to_build)

sln_config = "Debug|iPhone Simulator"
sln_dir = os.path.dirname(settings.sln_path)

instruments.CreateOrRestoreFromBackup(sln_dir, settings.files_for_backup)
instruments.RemoveProjectFromSolution(settings.sln_path, settings.projects_to_exclude)
instruments.CleanSolution(settings.mdtool, settings.sln_path)
instruments.BuildSolution(settings.mdtool, settings.sln_path, sln_config)

# instruments.DeleteBackups(sln_dir, settings.files_for_backup)