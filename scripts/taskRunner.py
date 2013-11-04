import os
from Core.LineConveyor.CommentRemover import CommentRemover
from Core.LineConveyor.LineConveyor import LineConveyor
from Core.LineConveyor.Stripper import Stripper
from utils.BuildConfigProvider import BuildConfigProvider
from utils.FromFileSettingsProvider import FromFileSettingsProvider

scriptFilePath = os.path.abspath(__file__)

scriptDir = os.path.dirname(scriptFilePath)
baseDir = os.path.join(scriptDir, os.pardir)

os.chdir(baseDir)

from Core.StepsRunner import StepsRunner


class TaskRunner:
	def __init__(self):
		self.configsProvider = BuildConfigProvider()
		self.settingsProvider = FromFileSettingsProvider()

		lineStripper = Stripper()
		commentRemover = CommentRemover()
		self.lineConveyor = LineConveyor()
		self.lineConveyor.addProcessor(lineStripper)
		self.lineConveyor.addProcessor(commentRemover)

	def run(self):
		settings = self.settingsProvider.fetchSettings()
		buildReadyConfigs = self.configsProvider.getConfigs(settings)

		for bc in buildReadyConfigs:
			self.runConfig(bc)

	def runConfig(self, config):
		content = self.getStepsContent(config)

		stepsRunner = StepsRunner(config, self.lineConveyor)
		stepsRunner.run(content)

	def getStepsContent(self, config):
		pathToSteps = config['steps']
		stepsFile = open(pathToSteps)

		content = stepsFile.read()
		return content

runner = TaskRunner()
runner.run()
