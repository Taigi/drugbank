__author__ = 'humberto'

from Levenshtein import distance
from drugBankAcessor_ET import  mapDrugBankFromFile


def levenshtein_dist(drugs):
    """
    Takes the drug names and computes the Levenshtein distance
    :param : a dictionary containing drug objects
    :rtype : list of tuples with the distance
    """
    dist = []
    drug_list = drugs.keys()
    # iterates over the keys
    for i in range(0, len(drug_list)):
        for j in range(i+1, len(drug_list)):
            # There are names that are not string or unicode
            if (isinstance(drugs[drug_list[i]].name, str) and isinstance(drugs[drug_list[j]].name, str)):
                d = distance(drugs[drug_list[i]].name, drugs[drug_list[j]].name)
                dist.append(((drugs[drug_list[i]].name, drugs[drug_list[j]].name), d))

    return dist


filename = '/Volumes/Local/Users/humberto/projects/drugbank/drugbank_short.xml'
drugs = mapDrugBankFromFile(filename)
print(levenshtein_dist(drugs))