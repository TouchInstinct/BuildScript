#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import argparse
from Core.FileContentProvider import FileContentProvider
from Core.LineConveyor.CommentRemover import CommentRemover
from Core.LineConveyor.TextConveyorPreprocessor import TextConveyorPreprocessor
from Core.LineConveyor.MacroResolver import MacroResolver
from Core.LineConveyor.Stripper import Stripper
from Core.LineConveyor.TextInclude import TextInclude
from commands.ValueProvider import ValueProvider
from utils.BuildConfigProvider.BuildConfigProvider import BuildConfigProvider
from utils.BuildConfigProvider.PredefinedMacrosBuildConfigProvider import PredefinedMacrosBuildConfigProvider
from utils.BuildConfigProvider.ResolvedBuildConfigProvider import ResolvedBuildConfigProvider
from utils.IncludeProcessor import IncludeProcessor
from utils.MacroProcessor import MacroProcessor
from utils.SettingsProvider.CmdArgsOverriderSettingsProvider import CmdArgsOverriderSettingsProvider
from utils.SettingsProvider.FromFileSettingsProvider import FromFileSettingsProvider
from Core.StepsRunner import StepsRunner

scriptFilePath = os.path.abspath(__file__)
scriptDir = os.path.dirname(scriptFilePath)

#baseDir = os.path.join(scriptDir, os.pardir)
#os.chdir(baseDir)


class TaskRunner:
	def __init__(self, settingsProvider, fileContentProvider, buildConfigProvider):
		assert settingsProvider is not None
		assert fileContentProvider is not None
		assert buildConfigProvider is not None

		self.settingsProvider = settingsProvider
		self.fileContentProvider = fileContentProvider
		self.configsProvider = buildConfigProvider

		lineStripper = Stripper()
		commentRemover = CommentRemover()

		macroProcessor = MacroProcessor()
		self.valueProvider = ValueProvider()
		macroResolver = MacroResolver(macroProcessor, self.valueProvider)

		includeProcessor = IncludeProcessor()
		textInclude = TextInclude(includeProcessor, self.fileContentProvider)

		# последовательность важна!
		# Сначала резолвим макросы, потом делаем включение файлов
		# Это позволяет использовать макросы в include выражениях
		self.textPreprocessor = TextConveyorPreprocessor()
		self.textPreprocessor.addProcessor(macroResolver)
		self.textPreprocessor.addProcessor(textInclude)

		self.linePreprocessor = TextConveyorPreprocessor()
		self.linePreprocessor.addProcessor(commentRemover)
		self.linePreprocessor.addProcessor(lineStripper)

	def run(self):
		rawSettings = self.settingsProvider.fetchSettings()
		buildReadyConfigs = self.configsProvider.getConfigs(rawSettings)

		for bc in buildReadyConfigs:
			self.valueProvider.setConfig(bc)
			self.runConfig(bc)

	def runConfig(self, config):
		content = self.getStepsContent(config)

		stepsRunner = StepsRunner(config, self.linePreprocessor, self.valueProvider)
		stepsRunner.run(content)

	def getStepsContent(self, config):
		pathToSteps = config['steps']

		content = self.fileContentProvider.fetchContent(pathToSteps)
		content = self.textPreprocessor.processText(content, self.textPreprocessor)

		return content

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	overrideArgs = parser.parse_known_args()[1]

	# TODO:  перенести в корень комапановки
	fromFileSettingsProvider = FromFileSettingsProvider()
	overrideWithCmdSetProvider = CmdArgsOverriderSettingsProvider(fromFileSettingsProvider, overrideArgs)

	fContentProvider = FileContentProvider()

	buildConfigProvider = BuildConfigProvider()
	predefineBuildConfigProvider = PredefinedMacrosBuildConfigProvider(buildConfigProvider)
	predefineBuildConfigProvider.addPredefineMacro('builder_path', scriptDir)

	resolvedBuildConfigProvider = ResolvedBuildConfigProvider(predefineBuildConfigProvider)


	runner = TaskRunner(overrideWithCmdSetProvider, fContentProvider, resolvedBuildConfigProvider)
	runner.run()