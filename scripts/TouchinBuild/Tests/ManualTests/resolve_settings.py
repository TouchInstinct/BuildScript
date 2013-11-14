from Core.ContentProviderBase import ContentProviderBase
from Core.LineConveyor.NullPreprocessor import NullPreprocessor
from Tests.Common.SettingsProviderStub import SettingsProviderStub
from taskRunner import TaskRunner
from utils.BuildConfigProvider.BuildConfigProvider import BuildConfigProvider
from utils.BuildConfigProvider.ResolvedBuildConfigProvider import ResolvedBuildConfigProvider

settingsText = """
build_tool = '/Applications/Xamarin\ Studio.app/Contents/MacOS/mdtool'
major_minor = '1.2'
build = '345'

configs = 'config1, config2'
steps = 'main_steps'

config1.version = '{@major_minor}'
config2.version = '{@major_minor}.{@build}'
"""

stepsFileContent = """
sh echo {@version}
"""

class ContentProviderMock(ContentProviderBase):
	def __init__(self):
		ContentProviderBase.__init__(self)

	def fetchContent(self, key):
		if key == 'main_steps':
			return stepsFileContent
		else:
			raise Exception(key)


settingsProvider = SettingsProviderStub(settingsText)

buildConfigProvider = BuildConfigProvider()
resolvedBuildConfigProvider = ResolvedBuildConfigProvider(buildConfigProvider)

contentProvider = ContentProviderMock()
preprocessor = NullPreprocessor()

taskRunner = TaskRunner(settingsProvider, contentProvider, resolvedBuildConfigProvider, preprocessor, {})

taskRunner.run()

