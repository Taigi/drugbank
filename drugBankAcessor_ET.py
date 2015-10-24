__author__ = 'root'


import xml.etree.cElementTree as ET

path = '/home/iva/DMKM/DrugBank/'

tree = ET.ElementTree(file=path+'drugbank.xml')
# print tree
# root = tree.getroot()
# root.tag, root.attrib
# for child_of_root in root:
#     print child_of_root.tag, child_of_root.attrib
print 'find direct elements with tag drug'
count = 0
for node in tree.findall('{http://www.drugbank.ca}drug'):
    #print node.tag, node.attrib
    count += 1
print count

print 'find children elements with tag drug'
#child elements
count = 0
for node in tree.findall('.//{http://www.drugbank.ca}drug'):
    #print node.tag, node.attrib
    count += 1

print count