__author__ = 'humberto'

import editdistance
import numpy as np
from drugBankAcessor_ET import  mapDrugBankFromFile


def levenshtein_dist(text_list):
    """
    Takes the drug names and computes the Levenshtein distance
    :param : a dictionary containing drug objects
    :rtype : list of tuples with the distance
    """
    dist = np.zeros(shape=(len(text_list), len(text_list)))
    # iterates over the keys
    for i in range(0, len(text_list)):
        for j in range(i+1, len(text_list)):
            # There are names that are not string or unicode
            if (isinstance(text_list[i], str) and isinstance(text_list[j], str)):
                d = editdistance.eval(text_list[i], text_list[j])
                dist[i, j] = d
                dist[j, i] = d


    return dist

