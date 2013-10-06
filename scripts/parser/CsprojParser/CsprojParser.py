from parser.CsprojParser.Csproj import Csproj
from parser.CsprojParser.CsprojLineParser import CsprojLineParser


class CsprojParser:
	def __init__(self, line_collection):
		assert line_collection is not None

		self.line_collection = line_collection
		self.projects_dict = {}

	def parse(self):

		settings = []
		for line in self.line_collection:
			settings.append(self.__parse_line(line))

		for s in settings:
			csproj = self.__fetchProject(s.appName)
			s.apply(csproj)

	def __fetchProject(self, project_name):
		assert project_name is not None

		csproj = self.projects_dict.get(project_name, Csproj(project_name))
		self.projects_dict[project_name] = csproj

		return csproj

	def __parse_line(self, line):
		line_parser = CsprojLineParser()
		setting = line_parser.parse(line)

		return setting