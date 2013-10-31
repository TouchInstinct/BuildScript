class BuildConfigProvider:
	def getBuildReadyConfigs(self, settingsDict, buildReadyList):
		assert settingsDict is not None
		assert buildReadyList is not None

		for key in settingsDict:
			value = settingsDict[key]

			if type(value) is dict:
				self.getBuildReadyConfigs(value, buildReadyList)

			elif key == 'build_ready' and value == 'true':
				buildReadyList.append(settingsDict)
				break


