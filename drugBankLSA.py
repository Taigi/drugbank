__author__ = 'humberto'

from drugBankAcessor_ET import mapDrugBankFromFile
import nltk
import matplotlib.pyplot as plt
# from textmining import TermDocumentMatrix, simple_tokenize_remove_stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial.distance import *
from sklearn.decomposition import PCA
from nltk.stem.porter import PorterStemmer
import string
import numpy as np
import re as re
from itertools import chain

def tokenize(text):
    tokens = nltk.word_tokenize(text.lower())
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems

def cosine(vector1, vector2):
    """
    related documents j and q are in the concept space by comparing the vectors :
    cosine  = ( V1 * V2 ) / ||V1|| x ||V2||
    """
    return float(np.dot(vector1,vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))

# Move to accessor
def drug_term_dictionary(drugs, kys, attr="description"):
    if type(attr) is not list:
        attrs = [attr]
    else:
        attrs = attr

    token_list = [None] * len(kys)
    n_non_empty_drugs = 0
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    for i in kys.keys():
        # Add more text processing: remove numbers, etc
        text = ''
        for a in attrs:
            text = text + ' ' + getattr(drugs[kys[i]], a)
        text = regex.sub('', text)
        if len(text) > 0:
            n_non_empty_drugs += 1
            token_list[i] = text.lower()#.translate(string.punctuation)
    print(len(drugs) - n_non_empty_drugs, " drugs found with empty fields")
    return token_list

def drug_term_dictionary2(drugs, attr="description"):
    token_dict = {}
    drug_list = drugs.keys()
    n_non_empty_drugs = 0
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    for d in drug_list:
        # Add more text processing: remove numbers, etc
        text = getattr(drugs[d], attr)
        text = regex.sub('', text)
        if len(text) > 0:
            n_non_empty_drugs += 1
            token_dict[d] = text.lower()#.translate(string.punctuation)
    print(len(drug_list) - n_non_empty_drugs, " drugs found with empty " + attr + " field")
    return token_dict

def intersection_index(list_a, list_b):
    """
    Returns two lists containing the index of the elements in list_a found in list_b
    and the index of elements of list_b contained in list_a

    :param : two lists
    :rtype : object
    """
    int_index_ab = []
    int_index_ba = []
    for i in range(0, len(list_a)):
        j = 0
        found = False
        while j < len(list_b) and not found:
            if list_a[i] == list_b[j]:
                found = True
                int_index_ab.append(i)
                int_index_ba.append(j)
            j += 1
    return int_index_ab, int_index_ba

def upper_tri_as_list(matr):
    tri_list = []
    n = matr.shape[0]
    # iterates over the keys
    for i in range(0,n):
        for j in range(i+1, n):
            tri_list.append(matr[i,j])
    return tri_list

# Reads the drugbank ids given an index
# Move to accessor
def label_idx(labels, nclust):
    ret = dict()
    for c in range(nclust):
        l = []
        for i in range(len(labels)):
            if labels[i] == c:
                l.append(i)
        ret[c] = l
    return ret

def idx_to_id(idx, ids_dict):
    ret = []
    for i in idx:
        ret.append(ids_dict[i])
    return ret