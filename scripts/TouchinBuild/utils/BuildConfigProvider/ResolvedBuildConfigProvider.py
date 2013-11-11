from Core.BuildConfigProviderBase import BuildConfigProviderBase
from Core.DependencyResolver.SettingsResolver import SettingsResolver


class ResolvedBuildConfigProvider(BuildConfigProviderBase):
	def __init__(self, buildConfigProvider):
		BuildConfigProviderBase.__init__(self)
		assert buildConfigProvider is not None

		self.inner = buildConfigProvider

	def getConfigs(self, rootConfig):
		unresolvedBuildConfigs = self.inner.getConfigs(rootConfig)
		resolvedBuildConfigs = []

		for bc in unresolvedBuildConfigs:
			resolver = SettingsResolver(bc)
			resolvedBuildConfig = resolver.resolveSettings()

			resolvedBuildConfigs.append(resolvedBuildConfig)

		return resolvedBuildConfigs