import re


class SlnPatcher:
	def __init__(self, pathToSlnFile):
		self._sln_path = pathToSlnFile
		self._sln_file = None

	def removeProjects(self, project_names):
		self.__openSlnFile()
		content = self.ReadSlnFileContent()

		new_content = self.RemoveProjectSectionsFrom(content, project_names)

		self.__rewriteSlnFile(new_content)
		self.__closeSlnFile()

	def __openSlnFile(self):
		self._sln_file = open(self._sln_path, 'r+')

	def __closeSlnFile(self):
		self._sln_file.close()

	def ReadSlnFileContent(self):
		content = self._sln_file.read()
		return content

	def __rewriteSlnFile(self, content):
		self._sln_file.seek(0)
		self._sln_file.write(content)
		self._sln_file.truncate()

	def RemoveProjectSectionsFrom(self, sln_file_content, project_names):
		for pn in project_names:
			reg_pattern = r'\n*Project.*?"{0}".*?\n*EndProject'.format(pn)
			sln_file_content = re.sub(reg_pattern, "", sln_file_content)

		return sln_file_content
