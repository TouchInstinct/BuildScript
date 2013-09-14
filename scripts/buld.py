from subprocess import call
import settings

# print("all projects:")
# print(settings.all_projects)

# project_to_remove = settings.projects_to_exclude[0];
# print("project to remove:")
# print(project_to_remove);


# projects_to_build = settings.all_projects[:]
# projects_to_build.remove(project_to_remove)

# print("projects to build:")
# print(projects_to_build)

sln_config = "Debug|iPhone Simulator 6.0"

build_cmd_pattern = '{0} -v build "--configuration:{1}" "--target:Build" {2}'
build_cmd_text = build_cmd_pattern.format(settings.mdtool, sln_config, settings.sln_path)
print(build_cmd_text)
ret_code = call(build_cmd_text, shell=True)
print('finished with return code: {0}'.format(ret_code))

