import xml.etree.ElementTree as eT

androidNs = 'http://schemas.android.com/apk/res/android'
eT.register_namespace('android', androidNs)

tree = eT.parse('data.xml')
root = tree.getroot()

print root.attrib

root.set('myAtr', 'myValue')
root.set('{{{0}}}myAtr'.format(androidNs), '777')
root.set('android:MyAttribute', 'Rustam')

tree.write('output.xml', xml_declaration=True, encoding='utf-8', method="xml")

print root.tag

