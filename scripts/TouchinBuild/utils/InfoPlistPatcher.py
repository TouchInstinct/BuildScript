import xml.etree.ElementTree as eT


class InfoPlistPatcher():
	def __init__(self, infoPlistPath):
		self.__infoPlistPath = infoPlistPath

	def AddOrReplace(self, key_value_dict):
		tree = eT.parse(self.__infoPlistPath)
		plist_dict = tree.getroot().find('dict')

		for keyName in key_value_dict:
			value = key_value_dict[keyName]
			if type(value) is str:
				self.AppendOrReplaceValueByKey(keyName, value, plist_dict)
			else:
				self.AppendOrReplaceValuesByKey(keyName, value, plist_dict)

		tree.write(self.__infoPlistPath, xml_declaration=True, encoding='UTF-8', method="xml")

	def AppendOrReplaceValueByKey(self, key_name, value, dict_element):
		key_index = self.FindIndexByKey(key_name, dict_element)
		element_exists = key_index >= 0

		if element_exists:
			self.ReplaceValueByKeyIndex(key_index, value, dict_element)
		else:
			self.AppendKeyValue(key_name, value, dict_element)

	def AppendOrReplaceValuesByKey(self, keyName, valuesArr, dictElement):
		keyIndex = self.FindIndexByKey(keyName, dictElement)
		elementExists = keyIndex >= 0

		if elementExists:
			self.ReplaceValuesByKeyIndex(keyIndex, valuesArr, dictElement)
		else:
			self.AppendValues(keyName, valuesArr, dictElement)

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

	def ReplaceValuesByKeyIndex(self, keyIndex, valueArr, dict_element):
		valuesIndex = keyIndex + 1
		arrayElement = dict_element[valuesIndex]

		children = arrayElement.findall('string')
		for ch in children:
			arrayElement.remove(ch)

		self.fillArrayElementWithValues(arrayElement, valueArr)

	def AppendKeyValue(self, keyName, value, dict_element):
		key_element = self.createKeyElement(keyName)
		value_element = self.createValueElement(value)

		dict_element.append(key_element)
		dict_element.append(value_element)

	def AppendValues(self, keyName, valuesArr, parentElement):
		keyElement = self.createKeyElement(keyName)

		arrayElement = eT.Element('array')
		self.fillArrayElementWithValues(arrayElement, valuesArr)

		parentElement.append(keyElement)
		parentElement.append(arrayElement)

	def createKeyElement(self, keyName):
		keyElement = eT.Element('key')
		keyElement.text = keyName

		return keyElement

	def createValueElement(self, value):
		valueElement = eT.Element('string')
		valueElement.text = value

		return valueElement

	def fillArrayElementWithValues(self, arrayElement, values):
		for value in values:
			valueElement = self.createValueElement(value)
			arrayElement.append(valueElement)





