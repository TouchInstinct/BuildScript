class BuildConfigProvider:
	def getConfigs(self, rootConfig):
		leafs = []
		self.traverseDict(None, rootConfig, leafs)

		configs = []
		for l in leafs:
			config = self.fetchConfigFromLeafWrapper(l)
			configs.append(config)

		return configs

	def traverseDict(self, parent, dictForTraverse, leafs):
		wrapper = {
			'parent' : parent,
			'dict' : dictForTraverse
		}

		isLeaf = True
		for key in dictForTraverse:
			value = dictForTraverse[key]

			if type(value) is dict:
				isLeaf = False
				self.traverseDict(wrapper, value, leafs)

		if isLeaf:
			leafs.append(wrapper)

	def fetchConfigFromLeafWrapper(self, leafWrapper):
		ancestors = self.getAncestorsFor(leafWrapper)

		unionConf = {}
		for a in ancestors:
			unionConf.update(a['dict'])

		return unionConf

	def getAncestorsFor(self, leaf):
		ancestors = [leaf]
		parent = leaf['parent']

		while parent is not None:
			ancestors.append(parent)
			parent = parent['parent']

		ancestors.reverse()
		return ancestors