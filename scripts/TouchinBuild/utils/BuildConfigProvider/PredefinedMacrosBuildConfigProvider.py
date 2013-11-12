from Core.BuildConfigProviderBase import BuildConfigProviderBase


class PredefinedMacrosBuildConfigProvider(BuildConfigProviderBase):
	def __init__(self, buildConfigProvider):
		BuildConfigProviderBase.__init__(self)
		assert buildConfigProvider is not None

		self.inner = buildConfigProvider
		self.predefine = {}

	def getConfigs(self, rootConfig):
		configsWithoutPreDef = self.inner.getConfigs(rootConfig)
		configsWithPreDef = []

		for bc in configsWithoutPreDef:
			for key in self.predefine:
				if key not in bc:
					bc[key] = self.predefine[key]

			configsWithPreDef.append(bc)

		return configsWithPreDef

	def addPredefineMacro(self, key, value):
		assert key is not None
		assert value is not None

		self.predefine[key] = value
