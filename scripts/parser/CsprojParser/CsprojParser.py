from parser.CsprojParser.Csproj import Csproj
from parser.CsprojParser.CsprojLineParser import CsprojLineParser


class CsprojParser:
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
			csproj = self.__fetchProject(s.appName)
			s.apply(csproj)

	def __fetchProject(self, project_name):
		assert project_name is not None

		csproj = self.projects_dict.get(project_name, Csproj(project_name))
		self.projects_dict[project_name] = csproj

		return csproj

	def __parse_line(self, line):
		line_parser = CsprojLineParser(self._value_provider)
		setting = line_parser.parse(line)

		return setting