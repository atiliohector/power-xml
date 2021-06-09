import xml.etree.ElementTree as ET

root = ET.parse('NFe_assinada.xml').getroot()

for i in root:
    print(i.text, i.tag)   