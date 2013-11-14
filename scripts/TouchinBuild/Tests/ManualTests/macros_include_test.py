from Core.ContentProviderBase import ContentProviderBase
from Core.LineConveyor.NullPreprocessor import NullPreprocessor
from Tests.Common.SettingsProviderStub import SettingsProviderStub
from taskRunner import TaskRunner
from utils.BuildConfigProvider.BuildConfigProvider import BuildConfigProvider

settingsText = """
build_tool = '/Applications/Xamarin\ Studio.app/Contents/MacOS/mdtool'
version = '0.0.0'
configs = 'config1, config2'
steps = 'main_steps'

config1.sub_steps = 'sub_steps1'
config2.sub_steps = 'sub_steps2'
"""

stepsFileContent = """
<include '{@sub_steps}'>
"""

subSteps1Content = """
sh echo One
"""

subSteps2Content = """
sh echo Two
"""

class ContentProviderMock(ContentProviderBase):
	def __init__(self):
		ContentProviderBase.__init__(self)

	def fetchContent(self, key):
		if key == 'sub_steps1':
			return subSteps1Content
		elif key == 'sub_steps2':
			return subSteps2Content
		elif key == 'main_steps':
			return stepsFileContent
		else:
			raise Exception(key)


settingsProvider = SettingsProviderStub(settingsText)
contentProvider = ContentProviderMock()

buildConfigProvider = BuildConfigProvider()
preprocessor = NullPreprocessor()

taskRunner = TaskRunner(settingsProvider, contentProvider, buildConfigProvider, preprocessor)

taskRunner.run()
