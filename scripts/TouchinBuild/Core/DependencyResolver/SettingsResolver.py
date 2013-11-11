from Core.DependencyResolver.DependencyResolver import DependencyResolver
from Core.DependencyResolver.Node import Node
from Core.LineConveyor.MacroResolver import MacroResolver
from commands.ValueProvider import ValueProvider
from utils.MacroProcessor import MacroProcessor


class SettingsResolver:
	def __init__(self, settingsDictionary):
		assert settingsDictionary is not None

		self.settings = settingsDictionary.copy()
		self.nodeStorage = {}
		self.macroProcessor = MacroProcessor()

		self.valueProvider = ValueProvider()
		self.valueProvider.setConfig(self.settings)


	def resolveSettings(self):

		self.fillNodesStorage()
		unresolved = self.nodeStorage.values()

		dependencyResolver = DependencyResolver()
		resolved = dependencyResolver.resolve(unresolved)

		self.resolveSettingValues(resolved)
		return self.settings

	def fillNodesStorage(self):

		for key in self.settings:
			node = self.fetchNodeByKey(key)

			value = self.settings[key]
			macroNames = self.macroProcessor.getSymbols(value)

			for symbol in macroNames:
				name = self.macroProcessor.getNameByMacroName(symbol)
				dependency = self.fetchNodeByKey(name)

				node.addEdge(dependency)

	def fetchNodeByKey(self, key):
		assert key is not Node

		node = self.nodeStorage.get(key, Node(key))
		self.nodeStorage[key] = node

		return node

	def resolveSettingValues(self, resolvedDependencies):
		macroResolver = MacroResolver(self.macroProcessor, self.valueProvider)

		for node in resolvedDependencies:
			unresolvedSettingValue = self.settings[node.name]
			resolvedSettingValue = macroResolver.processText(unresolvedSettingValue)

			self.settings[node.name] = resolvedSettingValue