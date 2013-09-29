import xml.etree.ElementTree as ET

def AppendKeyValue(key_name, value, dict_element):
	key_element = ET.Element('key')
	key_element.text = key_name

	value_element = ET.Element('string')
	value_element.text = value

	dict_element.append(key_element)
	dict_element.append(value_element)

def ReplaceValueByKeyIndex(key_element_index, value, dict_element):
	value_index = key_element_index + 1
	value_element = dict_element[value_index]
	value_element.text = value

def FindIndexByKey(key_name, dict_element):
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

def AppendOrReplaceValueByKey(key_name, value, dict_element):
	key_index = FindIndexByKey(key_name, dict_element)
	element_exists = key_index >= 0

	if element_exists:
		ReplaceValueByKeyIndex(key_index, value, dict_element)
	else:
		AppendKeyValue(key_name, value, dict_element)

def AppendOrReplace(key_value_dict, abs_plist_path):
	tree = ET.parse(abs_plist_path)
	plist_dict = tree.getroot().find('dict')

	for key_name in key_value_dict:
		AppendOrReplaceValueByKey(key_name, key_value_dict[key_name], plist_dict)

	tree.write(abs_plist_path)