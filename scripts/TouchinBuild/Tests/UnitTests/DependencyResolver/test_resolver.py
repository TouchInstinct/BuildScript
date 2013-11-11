import unittest
from Core.DependencyResolver.DependencyResolver import DependencyResolver
from Core.DependencyResolver.Node import Node


class TestDependencyResolver(unittest.TestCase):
	def setUp(self):
		self.resolver = DependencyResolver()

	def test_OneConnectedness(self):
		node1 = Node('node1')
		node2 = Node('node2')

		node3 = Node('node3')
		node3.addEdge(node1)
		node3.addEdge(node2)

		node4 = Node('node4')
		node4.addEdge(node3)
		node4.addEdge(node1)

		unresolved = [node4, node3, node2, node1]
		resolved = self.resolver.resolve(unresolved)

		self.assertEqual(4, len(resolved))

		self.assertEqual(node1, resolved[0])
		self.assertEqual(node2, resolved[1])
		self.assertEqual(node3, resolved[2])
		self.assertEqual(node4, resolved[3])

