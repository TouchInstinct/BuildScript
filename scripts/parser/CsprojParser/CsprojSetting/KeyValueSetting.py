from parser.CsprojParser.CsprojSetting.CsprojSettingBase import CsprojSettingBase


class KeyValueSetting(CsprojSettingBase):
	def __init__(self, key, value):
		self._notNoneOrEmpty(key)
		self._notNoneOrEmpty(value)

		self.key = key
		self.value = value

	def apply(self, csproj):
		assert csproj is not None

		csproj.settings[self.key] = self.value
