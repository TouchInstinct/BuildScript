class DependencyResolver:
	def __init__(self):
		pass

	def resolve(self, unresolved):
		assert unresolved is not None
		resolved = []

		while len(unresolved) > 0:
			node = unresolved[0]
			self.resolveNode(node, resolved, unresolved, [])

		return resolved

	def resolveNode(self, node, resolved, unresolved, seen):
		assert node is not None
		assert resolved is not None
		assert seen is not None

		seen.append(node)

		for dependency in node.edges:
			if dependency not in resolved:
				self.guardNotCircularReference(node, dependency, seen)
				self.resolveNode(dependency, resolved, unresolved, seen)

		resolved.append(node)
		unresolved.remove(node)
		seen.remove(node)

	def guardNotCircularReference(self, start, dependency, seen):
		assert start is not None
		assert dependency is not None
		assert seen is not None

		if dependency in seen:
			raise Exception('Circular reference detected: {0} -> {1}'.format(start.name, dependency.name))

