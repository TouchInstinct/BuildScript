import xml.etree.ElementTree as eT

class XmlPatcher:
	def __init__(self, path):
		assert path is not None

		self.path = path
		self.namespaces = {}

	def parse(self):
		return eT.parse(self.path)

	def write(self, tree):
		tree.write(self.path, xml_declaration=True, encoding="UTF-8", method="xml")

	def regNamespace(self, nsKey, nsValue):
		assert nsKey is not None
		assert nsValue is not None

		eT.register_namespace(nsKey, nsValue)

	def getNameWithNs(self, originalName, namespace):
		assert originalName is not None
		assert namespace is not None

		# {someNamespace}OriginalName
		return '{{{0}}}{1}'.format(namespace, originalName)
