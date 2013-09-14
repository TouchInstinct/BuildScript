from subprocess import call
import os
import re

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

sln_config = "Debug|iPhone Simulator"
build_cmd_pattern = '{0} -v build "--configuration:{1}" "--target:Build" {2}'
# build_cmd_text = build_cmd_pattern.format(settings.mdtool, sln_config, settings.sln_path)

# print(build_cmd_text)
# ret_code = call(build_cmd_text, shell=True)
# print('finished with return code: {0}'.format(ret_code))

sln_dir = os.path.dirname(settings.sln_path)
sln_file = open(settings.sln_path)
sln_file_content = sln_file.read()
# print(sln_file_content)

project_description_re = re.compile(r' = "(?P<project_name>\S+)", "(?P<project_rel_path>[\S\\]+csproj)"')
match_iter = project_description_re.finditer(sln_file_content)

project_descriptions = [m.groupdict() for m in match_iter]
for project_description in project_descriptions:
	rel_path = project_description['project_rel_path'].replace('\\', '/')
	abs_path = os.path.join(sln_dir, rel_path)
	build_cmd_text = build_cmd_pattern.format(settings.mdtool, sln_config, abs_path)
	print(build_cmd_text)
	ret_code = call(build_cmd_text, shell=True)
	print('finished with return code: {0}'.format(ret_code))
