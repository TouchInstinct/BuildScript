import utils.sln.sln_toolkit_base as sln


class SolutionToolkit(sln.SolutionToolkitBase):
	def __init__(self, pathToSlnFile):
		self._sln_path = pathToSlnFile
		self._sln_file = None

	def RemoveProjects(self, project_names):
		self.OpenSlnFile()
		content = self.ReadSlnFileContent()

		new_content = self.RemoveProjectSectionsFrom(content, project_names)

		self.RewriteSlnFile(new_content)
		self.CloseSlnFile()

	def OpenSlnFile(self):
		self._sln_file = open(self._sln_path, 'r+')

	def CloseSlnFile(self):
		self._sln_file.close()

	def ReadSlnFileContent(self):
		content = self._sln_file.read()
		return content

	def RewriteSlnFile(self, content):
		self._sln_file.seek(0)
		self._sln_file.write(content)
		self._sln_file.truncate()