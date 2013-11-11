class Node:
	def __init__(self, name):
		assert name is not None

		self.name = name
		self.edges = []

	def addEdge(self, node):
		assert node is not None
		assert node not in self.edges

		self.edges.append(node)