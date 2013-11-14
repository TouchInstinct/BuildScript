import unittest
from utils.ManifestPatcher import ManifestPatcher


class TestManifestPatcher(unittest.TestCase):
	def setUp(self):
		self.patcher = ManifestPatcher('somePath')

	def test_parseRawName(self):
		nameInfo1 = self.patcher.parseRawName('simpleName')
		self.assertEqual(None, nameInfo1['prefix'])
		self.assertEqual('simpleName', nameInfo1['original_name'])

		nameInfo2 = self.patcher.parseRawName('prefix:originalName')
		self.assertEqual('prefix', nameInfo2['prefix'])
		self.assertEqual('originalName', nameInfo2['original_name'])
