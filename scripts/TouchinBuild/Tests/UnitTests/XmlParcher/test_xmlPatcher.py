import unittest
from utils.XmlPatcher import XmlPatcher


class TestXmlPatcher(unittest.TestCase):
	def setUp(self):
		self.patcher = XmlPatcher('somePath')

	def test_getNameWithNs(self):
		name = self.patcher.getNameWithNs('OriginalName', 'http://namespace')
		self.assertEqual('{http://namespace}OriginalName', name)
