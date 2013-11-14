import unittest
from CommandBuilders.InstallProfileCommandBuilder import InstallProfileCommandBuilder


class TestInstallProfileBuilder(unittest.TestCase):
	def setUp(self):
		self.prefix = 'MyProject'
		self.builder = InstallProfileCommandBuilder(self.prefix)

	def test_dstFileName(self):
		dstFileName = self.builder.fetchDstFileName('/Some/Path/MyProfile.ext')
		self.assertEqual(dstFileName, '{0}.MyProfile.ext'.format(self.prefix))

	def test_dstPath(self):
		dstPath = self.builder.getDestinationPath('/Some/Path/MyProfile.ext')
		self.assertEqual('~/Library/MobileDevice/Provisioning Profiles/{0}.MyProfile.ext'.format(self.prefix), dstPath)