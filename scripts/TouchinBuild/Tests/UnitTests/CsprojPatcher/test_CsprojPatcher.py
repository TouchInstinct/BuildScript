import unittest
from utils.CsprojPatcher import CsprojPatcher


class TestCsprojPatcher(unittest.TestCase):
	def setUp(self):
		self.patcher = CsprojPatcher('NotExists.sln')

	def test_CheckPropertyGroupCondition(self):
		self.checkFit(" '$(Configuration)|$(Platform)' == 'Debug|iPhoneSimulator' ", 'Debug|iPhoneSimulator')
		self.checkFit(" '$(Configuration)|$(Platform)'=='Debug|iPhoneSimulator' ", 'Debug|iPhoneSimulator')
		self.checkFit("'$(Configuration)|$(Platform)' == 'Debug|iPhoneSimulator'", 'Debug|iPhoneSimulator')
		self.checkFit("'$(Configuration)|$(Platform)'=='Debug|iPhoneSimulator'", 'Debug|iPhoneSimulator')

		self.checkFit(" '$(Configuration)' == '' ", '')
		self.checkFit(" '$(Configuration)'=='' ", '')
		self.checkFit("'$(Configuration)' == ''", '')
		self.checkFit("'$(Configuration)'==''", '')

	def checkFit(self, conditionAttrValue, slnConfig):
		isFit = self.patcher.IsValueFitFor(slnConfig, conditionAttrValue)
		self.assertTrue(True, isFit)

