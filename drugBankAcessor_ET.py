__author__ = 'root'


import xml.etree.cElementTree as ET
from Classification import Classification
from Drug import Drug
from Sequence import Sequence

def mapDrugBankFromFile(filename):
    file = open(filename, 'r')
    tree = ET.parse(file)
    file.close()
    drugs = []
    # dictionary with the namespaces
    ns = {'drugbank': 'http://www.drugbank.ca', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}

    # iterate over all drugs - children of drugbank
    count = 0
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
        pharmacodynamics = drugtag.find('drugbank:pharmacodynamics',ns).text

        #check if any of the texts are None, primary and name shouldn't be none so not checking for them
        if description == None:
            description = ''
        if indication ==None:
            indication = ''
        if pharmacodynamics==None:
            pharmacodynamics = ''

        classification = None
        classificationtag = drugtag.find('drugbank:classification', ns)
        if classificationtag != None:
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
        synonyms = []
        synonymstag = drugtag.find('drugbank:synonyms', ns)
        for syn in synonymstag:
            synonyms.append(syn.text)

        international_brands = []
        ibstag = drugtag.find('drugbank:international-brands', ns)
        for ib in ibstag:
            ibname = ib.find('drugbank:name', ns).text
            international_brands.append(ibname)

        categories = []
        catstag = drugtag.find('drugbank:categories', ns)
        for cat in catstag:
            catname = cat.find('drugbank:category', ns).text
            categories.append(catname)

        sequences = []
        seqstag = drugtag.find('drugbank:sequences', ns)
        if seqstag!= None:
            for seq in seqstag:
                seqdict = seq.attrib
                seqtype = seqdict.get('format')
                seqname = seq.text
                sequences.append(Sequence(seqname, seqtype))

        molecular_weight = 0.0
        molecular_formula = ''
        propstag = drugtag.find('drugbank:experimental-properties', ns)
        for prop in propstag:
            propkind = prop.find('drugbank:kind', ns).text
            if propkind == 'Molecular Weight':
                molecular_weight = prop.find('drugbank:value', ns).text
            if propkind == 'Molecular Formula':
                molecular_formula = prop.find('drugbank:value', ns).text

        pathways_drugs = []
        pathways_enzymes = []
        pathwaystag = drugtag.find('drugbank:pathways', ns)
        if pathwaystag != None:
            for pathwaytag in pathwaystag:
                drugstag = pathwaytag.find('drugbank:drugs', ns)
                for drugtag in drugstag:
                    drugid = drugtag.find('drugbank:drugbank-id', ns).text
                    pathways_drugs.append(drugid)
                enzymestag = pathwaytag.find('drugbank:enzymes', ns)
                if enzymestag != None:
                    for uniprot in enzymestag:
                        #uniprotid = enzymetag.find('drugbank:uniprot-id', ns).text
                        pathways_enzymes.append(uniprot.text)


        drug = Drug(primary, other_ids, name, description, indication, pharmacodynamics,
                    classification, synonyms, international_brands,
                    categories, sequences, molecular_weight, molecular_formula, pathways_drugs, pathways_enzymes)
        drugs.append(drug)

    return drugs

    #     drug.printout()
    #     count +=1
    # print count
#filename = '/home/iva/DMKM/DrugBank/drugbank.xml'
#filename = '/root/PycharmProjects/drugbank/sampleN.xml'
#mapDrugBankFromFile(filename)