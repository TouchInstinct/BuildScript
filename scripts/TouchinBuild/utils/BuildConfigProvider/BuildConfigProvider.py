from Core.BuildConfigProviderBase import BuildConfigProviderBase


class BuildConfigProvider(BuildConfigProviderBase):
	def __init__(self):
		BuildConfigProviderBase.__init__(self)

	def getConfigs(self, rootConfig):
		buildReadyConfigNames = self.fetchBuildReadyConfigNames(rootConfig)

		leafs = []
		self.traverseDict(None, None, rootConfig, leafs)

		configs = []
		for l in leafs:
			configInfo = self.fetchConfigInfoFromLeafWrapper(l)
			name = configInfo[0]
			config = configInfo[1]

			if name in buildReadyConfigNames:
				configs.append(config)

		return configs

	def fetchBuildReadyConfigNames(self, rootConfig):
		value = rootConfig['configs']
		names = value.split(',')
		names = [name.strip(' ') for name in names]

		return names

	def traverseDict(self, parent, key, dictForTraverse, leafs):
		wrapper = {
			'parent': parent,
			'dict': dictForTraverse,
			'name': key
		}

		isLeaf = True
		for key in dictForTraverse:
			value = dictForTraverse[key]

			if type(value) is dict:
				isLeaf = False
				self.traverseDict(wrapper, key, value, leafs)

		if isLeaf:
			leafs.append(wrapper)

	def fetchConfigInfoFromLeafWrapper(self, leafWrapper):
		ancestors = self.getAncestorsFor(leafWrapper)

		unionConf = {}
		for a in ancestors:
			dictionary = a['dict']
			for k in dictionary:
				value = dictionary[k]
				if type(value) is str:
					unionConf[k] = value

		return leafWrapper['name'], unionConf

	def getAncestorsFor(self, leaf):
		ancestors = [leaf]
		parent = leaf['parent']

		while parent is not None:
			ancestors.append(parent)
			parent = parent['parent']

		ancestors.reverse()
		return ancestors