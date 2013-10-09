from parser.ProjectParser.Project import Project
from parser.ProjectParser.ProjectLineParser import ProjectLineParser


class ProjectParser:
	def __init__(self, line_collection, value_provider):
		assert line_collection is not None
		assert value_provider is not None

		self._line_collection = line_collection
		self._value_provider = value_provider
		self.projects_dict = {}

	def parse(self):

		settings = []
		for line in self._line_collection:
			settings.append(self.__parse_line(line))

		for s in settings:
			project = self.__fetchProject(s.projectName)
			s.apply(project)

	def __fetchProject(self, project_name):
		assert project_name is not None

		project = self.projects_dict.get(project_name, Project(project_name))
		self.projects_dict[project_name] = project

		return project

	def __parse_line(self, line):
		line_parser = ProjectLineParser(self._value_provider, 'csproj')
		setting = line_parser.parse(line)

		return setting