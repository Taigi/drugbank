__author__ = 'root'


import xml.etree.cElementTree as ET
from Classification import Classification
from Drug import Drug

def mapDrugBankFromFile(filename):
    file = open(filename, 'r')
    tree = ET.parse(file)
    file.close()

    # dictionary with the namespaces
    ns = {'drugbank': 'http://www.drugbank.ca', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}

    # iterate over all drugs - children of drugbank

    for drugtag in tree.getroot():
        ids = drugtag.findall('drugbank:drugbank-id', ns)
        primary = drugtag.find("drugbank:drugbank-id[@primary='true']", ns).text
        other_ids = []
        for other in ids:
            if other.text != primary:
                if other.text ==None:
                    other.text = ''
                other_ids.append(other.text)

        name = drugtag.find('drugbank:name', ns).text
        description = drugtag.find('drugbank:description', ns).text
        indication = drugtag.find('drugbank:indication', ns).text

        #check if any of the texts are None, primary and name shouldn't be none so not checking for them
        if description == None:
            description = ''
        if indication ==None:
            indication = ''

        classificationtag = drugtag.find('drugbank:classification', ns)
        class_description = classificationtag.find('drugbank:description', ns).text
        direct_parent = classificationtag.find('drugbank:direct-parent', ns).text
        kingdom = classificationtag.find('drugbank:kingdom', ns).text
        superclass = classificationtag.find('drugbank:superclass', ns).text
        class_type = classificationtag.find('drugbank:class', ns).text
        subclass = classificationtag.find('drugbank:subclass', ns).text

        # check if any of the texts are None
        if class_description == None:
            class_description = ''
        if direct_parent == None:
            direct_parent = ''
        if kingdom == None:
            kingdom = ''
        if superclass == None:
            superclass = ''
        if subclass == None:
            subclass = ''
        classification =  Classification(class_description, direct_parent, kingdom, superclass,
                                         class_type, subclass)
#def __init__(self, primary_id, other_ids, name, international_brand, description, indication, classification=None):

        drug = Drug(primary, other_ids, name, '', description, indication, classification)
        drug.printout()



    # print tree
    # root = tree.getroot()
    # root.tag, root.attrib
    # for child_of_root in root:
    #     print child_of_root.tag, child_of_root.attrib
    # print 'find direct elements with tag drug'
    # count = 0
    # for node in tree.findall('drugbank:drug', ns):
    #     print node.tag, node.attrib
    #     count += 1
    # print count
    #
    # print 'find children elements with tag drug'
    # #child elements
    # count = 0
    # for node in tree.findall('.//drugbank:drug', ns):
    #     #print node.tag, node.attrib
    #     count += 1
    # print count

#filename = '/home/iva/DMKM/DrugBank/drugbank.xml'
filename = '/root/PycharmProjects/drugbank/sample.xml'
mapDrugBankFromFile(filename)