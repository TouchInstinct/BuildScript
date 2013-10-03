import re


class SolutionToolkitBase:
	def RemoveProjectSectionsFrom(self, sln_file_content, project_names):
		for pn in project_names:
			reg_pattern = r'\n*Project.*?"{0}".*?\n*EndProject'.format(pn)
			sln_file_content = re.sub(reg_pattern, "", sln_file_content)

		return sln_file_content

