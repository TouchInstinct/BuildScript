import xml.etree.ElementTree as eT


class Patcher:
	def __init__(self, csproj_abs_path):
		self._csproj_abs_path = csproj_abs_path

	def FetchPropertyGroup(self, sln_config_name):
		tree = eT.parse(self._csproj_abs_path)
		project_element = tree.getroot()
		property_group = self.GetPropertyGroupBy(project_element, sln_config_name)

		return  property_group


	def GetPropertyGroupBy(self, project_element, config_name):
		property_groups = project_element.findall('PropertyGroup')
		prop_group = None

		for pg_elem in property_groups:
			atr_value = pg_elem.get('Condition')
			is_fit = self.IsValueFitFor(config_name, atr_value)

			if is_fit:
				prop_group = pg_elem
				break

		return  prop_group


	def Remove(self, tag_names, sln_config_name):
		property_group = self.FetchPropertyGroup(sln_config_name)
		self.RemoveTagsFor(property_group, tag_names)


	def AddOrReplace(self, key_value_dict, sln_config_name):
		property_group = self.FetchPropertyGroup(sln_config_name)
		self.AddOrReplaceTagsFor(property_group, key_value_dict)


	def IsValueFitFor(self, config_name, condition_attr_value):
		result = config_name in condition_attr_value
		return result


	def RemoveTagsFor(self, property_group_element, tag_names):
		for tn in tag_names:
			elem_to_remove = property_group_element.find(tn)

			if elem_to_remove is not None:
				property_group_element.remove(elem_to_remove)


	def AddOrReplaceTagsFor(self, property_group_element, key_value_dict):
		for k in key_value_dict:
			v = key_value_dict[k]
			self.AppendOrReplaceValueByKey(k, v, property_group_element)


	def AppendOrReplaceValueByKey(self, tag_name, value, property_group_element):
		tag = property_group_element.find(tag_name)

		if tag is None:
			tag = eT.Element(tag_name)
			property_group_element.append(tag)

		tag.text = value