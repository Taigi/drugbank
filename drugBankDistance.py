__author__ = 'humberto'

from Levenshtein import distance
from Drug import Drug

def levenshtein_dist(drugs):
    dist = []
    drug_list = drugs.keys()
    # iterates over the
    for i in range(0, len(drug_list)):
        for j in range(i+1, len(drug_list)):
            # There are names that are not string or unicode
            if (isinstance(drugs[drug_list[i]].name, str) and isinstance(drugs[drug_list[j]].name, str)):
                d = distance(drugs[drug_list[i]].name, drugs[drug_list[j]].name)
                dist.append(((drugs[drug_list[i]].name, drugs[drug_list[j]].name), d))

    return dist
