from SettingsProvider.FromFileSettingsProvider import FromFileSettingsProvider
from utils.configs.BuildConfigProvider import BuildConfigProvider

settingsProvider = FromFileSettingsProvider()
settings = settingsProvider.fetchSettings()

buildReadyConfigs = []
configsProvider = BuildConfigProvider()
configsProvider.getBuildReadyConfigs(settings, buildReadyConfigs)

for bc in buildReadyConfigs:
	print bc
