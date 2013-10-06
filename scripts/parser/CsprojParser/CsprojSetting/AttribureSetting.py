from parser.CsprojParser.CsprojSetting.CsprojSettingBase import CsprojSettingBase


class AttributeSetting(CsprojSettingBase):
	def __init__(self, name, value):
		self._notNoneOrEmpty(name)
		self._notNoneOrEmpty(value)

		self.attribute_name = name
		self.attribute_value = value

	def apply(self, csproj):
		assert csproj is not None

		setattr(csproj, self.attribute_name, self.attribute_value)
