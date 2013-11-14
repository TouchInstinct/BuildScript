from utils.XmlPatcher import XmlPatcher

class ManifestPatcher(XmlPatcher):
	def __init__(self, manifestPath):
		assert manifestPath is not None

		XmlPatcher.__init__(self, manifestPath)

		self.androidNs = "http://schemas.android.com/apk/res/android"
		self.androidNsPrefix = 'android'

		self.namespaces[self.androidNsPrefix] = self.androidNs
		self.regNamespace(self.androidNsPrefix, self.androidNs)

	def AddOrReplaceManifestAtr(self, rawAtrName, atrValue):
		assert rawAtrName is not None
		assert atrValue is not None

		tree = self.parse()
		manifestElement = tree.getroot()

		name = self.fetchNameByRawName(rawAtrName)
		manifestElement.set(name, atrValue)

		self.write(tree)

	def fetchNameByRawName(self, rawName):
		nameInfo = self.parseRawName(rawName)
		name = self.fetchName(nameInfo)

		return name

	def parseRawName(self, rawName):
		"""rawName=(nsPrefix:)?OriginalName
		"""

		result = rawName.split(':')
		prefixExists = len(result) > 1

		nameInfo = {
			'prefix': result[0] if prefixExists else None,
			'original_name': result[1] if prefixExists else result[0]
		}

		return nameInfo

	def fetchName(self, nameInfo):
		assert nameInfo is not None

		nsPrefix = nameInfo['prefix']
		origName = nameInfo['original_name']

		namespace = self.namespaces.get(nsPrefix, None)
		name = self.getNameWithNs(origName, namespace) if nsPrefix else origName
		return name