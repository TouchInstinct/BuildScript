from parser.CsprojParser.CsprojSetting.CsprojSettingBase import CsprojSettingBase


class KeyValueSetting(CsprojSettingBase):
	def __init__(self, key, value):
		assert key is not None and key != ''
		assert value is not None and value != ''

		self.key = key
		self.value = value

	def apply(self, csproj):
		assert csproj is not None

		csproj.settings[self.key] = self.value
