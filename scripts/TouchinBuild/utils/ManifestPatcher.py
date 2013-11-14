import xml.etree.ElementTree as eT


class ManifestPatcher:
	def __init__(self, manifestPath):
		assert manifestPath is not None

		self.manifestPath = manifestPath

	def AddOrReplaceManifestAtr(self, atrName, atrValue):
		tree = eT.parse(self.manifestPath)
		manifestElement = tree.getroot().find('manifest')

		manifestElement.attrib[atrName] = atrValue

		tree.write(self.manifestPath, xml_declaration=True, encoding='UTF-8', method="xml")