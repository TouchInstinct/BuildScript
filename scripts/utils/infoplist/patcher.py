import xml.etree.ElementTree as eT


class Patcher():
	def __init__(self, infoPlistPath):
		self.__infoPlistPath = infoPlistPath

	def AddOrReplace(self, key_value_dict):
		tree = eT.parse(self.__infoPlistPath)
		plist_dict = tree.getroot().find('dict')

		for key_name in key_value_dict:
			self.AppendOrReplaceValueByKey(key_name, key_value_dict[key_name], plist_dict)

		tree.write(self.__infoPlistPath, xml_declaration=True, encoding='UTF-8', method="xml")

	def AppendOrReplaceValueByKey(self, key_name, value, dict_element):
		key_index = self.FindIndexByKey(key_name, dict_element)
		element_exists = key_index >= 0

		if element_exists:
			self.ReplaceValueByKeyIndex(key_index, value, dict_element)
		else:
			self.AppendKeyValue(key_name, value, dict_element)

	def FindIndexByKey(self, key_name, dict_element):
		all_keys_elements = dict_element.findall('key')

		is_exists = False
		index = 0

		for e in all_keys_elements:
			if e.text == key_name:
				is_exists = True
				break
			index += 1

		element_index = index * 2
		return element_index if is_exists else -1

	def ReplaceValueByKeyIndex(self, key_element_index, value, dict_element):
		value_index = key_element_index + 1
		value_element = dict_element[value_index]
		value_element.text = value

	def AppendKeyValue(self, key_name, value, dict_element):
		key_element = eT.Element('key')
		key_element.text = key_name

		value_element = eT.Element('string')
		value_element.text = value

		dict_element.append(key_element)
		dict_element.append(value_element)



