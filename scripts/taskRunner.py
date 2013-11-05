# -*- coding: utf-8 -*-
import os
import argparse
from Core.LineConveyor.CommentRemover import CommentRemover
from Core.LineConveyor.LineConveyor import LineConveyor
from Core.LineConveyor.MacroResolver import MacroResolver
from Core.LineConveyor.Stripper import Stripper
from commands.ValueProvider import ValueProvider
from utils.BuildConfigProvider import BuildConfigProvider
from utils.MacroProcessor import MacroProcessor
from utils.SettingsProvider.CmdArgsOverriderSettingsProvider import CmdArgsOverriderSettingsProvider
from utils.SettingsProvider.FromFileSettingsProvider import FromFileSettingsProvider

scriptFilePath = os.path.abspath(__file__)

scriptDir = os.path.dirname(scriptFilePath)
baseDir = os.path.join(scriptDir, os.pardir)

os.chdir(baseDir)

from Core.StepsRunner import StepsRunner


class TaskRunner:
	def __init__(self, settingsProvider):
		assert settingsProvider is not None

		self.settingsProvider = settingsProvider
		self.configsProvider = BuildConfigProvider()

		lineStripper = Stripper()
		commentRemover = CommentRemover()

		macroProcessor = MacroProcessor()
		self.valueProvider = ValueProvider()
		macroResolver = MacroResolver(macroProcessor, self.valueProvider)

		self.lineConveyor = LineConveyor()
		self.lineConveyor.addProcessor(lineStripper)
		self.lineConveyor.addProcessor(commentRemover)
		self.lineConveyor.addProcessor(macroResolver)

	def run(self):
		settings = self.settingsProvider.fetchSettings()
		buildReadyConfigs = self.configsProvider.getConfigs(settings)

		for bc in buildReadyConfigs:
			self.valueProvider.setConfig(bc)
			self.runConfig(bc)

	def runConfig(self, config):
		content = self.getStepsContent(config)

		stepsRunner = StepsRunner(config, self.lineConveyor, self.valueProvider)
		stepsRunner.run(content)

	def getStepsContent(self, config):
		pathToSteps = config['steps']
		stepsFile = open(pathToSteps)

		content = stepsFile.read()
		return content

parser = argparse.ArgumentParser()
overrideArgs = parser.parse_known_args()[1]

# TODO:  перенести в корень комапановки
fromFileSettingsProvider = FromFileSettingsProvider()
settingsProvider = CmdArgsOverriderSettingsProvider(fromFileSettingsProvider, overrideArgs)

runner = TaskRunner(settingsProvider)
runner.run()
