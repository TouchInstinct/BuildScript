# -*- coding: utf-8 -*-
import xml.etree.ElementTree as eT
eT.register_namespace('', "http://schemas.microsoft.com/developer/msbuild/2003")

class CsprojPatcher:
	def __init__(self, csproj_abs_path):
		self._csproj_abs_path = csproj_abs_path
		self._tree = None
		self._namespaces = {'ns': 'http://schemas.microsoft.com/developer/msbuild/2003'}


	def FetchPropertyGroup(self, slnConfigName):
		assert slnConfigName is not None

		self._tree = eT.parse(self._csproj_abs_path)
		projectElement = self._tree.getroot()

		property_group = self.GetPropertyGroupBy(projectElement, slnConfigName)
		return property_group

	def WriteTree(self):
		self._tree.write(self._csproj_abs_path, xml_declaration=True, encoding='utf-8', method="xml")


	def GetPropertyGroupBy(self, project_element, config_name):
		assert project_element is not None
		assert config_name is not None

		property_groups = project_element.findall('ns:PropertyGroup', self._namespaces)

		prop_group = None

		for pg_elem in property_groups:
			#  atr_value мб None  для первого PropertyGroup
			atr_value = pg_elem.get('Condition')
			is_fit = self.IsValueFitFor(config_name, atr_value)

			if is_fit:
				prop_group = pg_elem
				break

		return prop_group


	def Remove(self, tag_names, sln_config_name):
		property_group = self.FetchPropertyGroup(sln_config_name)
		self.RemoveTagsFor(property_group, tag_names)
		self.WriteTree()


	def AddOrReplace(self, key_value_dict, sln_config_name):
		assert key_value_dict is not None
		assert sln_config_name is not None

		property_group = self.FetchPropertyGroup(sln_config_name)
		self.AddOrReplaceTagsFor(property_group, key_value_dict)
		self.WriteTree()


	def IsValueFitFor(self, config_name, condition_attr_value):
		if condition_attr_value is None:
			result = config_name == '' or config_name is None
		else:
			# '$(Configuration)|$(Platform)' == 'Debug|iPhoneSimulator'
			configValue = condition_attr_value.split('==')[1]
			configValue = configValue.strip()

			result = "'{0}'".format(config_name) == configValue

		return result


	def RemoveTagsFor(self, property_group_element, tag_names):
		for tn in tag_names:
			elem_to_remove = property_group_element.find(tn)

			if elem_to_remove is not None:
				property_group_element.remove(elem_to_remove)


	def AddOrReplaceTagsFor(self, property_group_element, key_value_dict):
		assert property_group_element is not None
		assert key_value_dict is not None

		for k in key_value_dict:
			v = key_value_dict[k]
			self.AppendOrReplaceValueByKey(k, v, property_group_element)


	def AppendOrReplaceValueByKey(self, tag_name, value, property_group_element):
		assert tag_name is not None
		assert value is not None
		assert property_group_element is not None

		tag = property_group_element.find('ns:{0}'.format(tag_name), self._namespaces)

		if tag is None:
			tag = eT.Element(tag_name)
			property_group_element.append(tag)

		tag.text = value