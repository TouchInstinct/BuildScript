from parser.CsprojParser.CsprojSetting.CsprojSettingBase import CsprojSettingBase


class AttributeSetting(CsprojSettingBase):
	def __init__(self, name, value):
		self.attribute_name = name
		self.attribute_value = value

	def apply(self, csproj):
		setattr(csproj, self.attribute_name, self.attribute_value)
