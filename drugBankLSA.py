__author__ = 'humberto'

from drugBankAcessor_ET import mapDrugBankFromFile
import nltk
import matplotlib.pyplot as plt
from textmining import TermDocumentMatrix, simple_tokenize_remove_stopwords
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

def drug_term_dictionary(drugs, attr="description"):
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


filename = '/Volumes/Local/Users/humberto/projects/drugbank/drugbank.xml'
drugs = mapDrugBankFromFile(filename)

#
drug_desc =  drug_term_dictionary(drugs, attr="description")
drug_pharma =  drug_term_dictionary(drugs, attr="pharmacodynamics")

# Read description
tfidf_desc = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs_desc = tfidf_desc.fit_transform(drug_desc.values())

# Read pharcacology
tfidf_pharma = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs_pharma = tfidf_pharma.fit_transform(drug_pharma.values())

print("Description tf-idf matrix dim: ", tfs_desc.A.shape)
print("Pharmacology tf-idf matrix dim: ", tfs_pharma.A.shape)

# matrix distances
dist_desc = squareform(pdist(tfs_desc.A, cosine))
dist_pharma = squareform(pdist(tfs_pharma.A, cosine))

idx_desc, idx_pharma = intersection_index(drug_desc.keys(), drug_pharma.keys())

print(len(idx_desc))
print(len(idx_pharma))

dist_desc_spliced = np.triu(dist_desc[np.ix_(idx_desc, idx_desc)])
dist_pharma_spliced = np.triu(dist_pharma[np.ix_(idx_pharma, idx_pharma)])


# Plot desc distance vs pharma distance
x = list(chain.from_iterable(dist_desc_spliced))
y = list(chain.from_iterable(dist_pharma_spliced))

print(len(x))
print(len(y))

plt.scatter(x, y, alpha=0.75)
plt.axis('tight')
plt.xlabel('description tf-idf cosine distance')
plt.ylabel('pharmacodynamics tf_idf cosine distance')
plt.savefig('desc_vs_pharma.png')


# pca = PCA()
# pca.fit(tfs.A)
# print(sum(pca.explained_variance_ratio_[:1000]))

# plt.figure(1, figsize=(4, 3))
# plt.clf()
# plt.axes([.2, .2, .7, .7])
# plt.plot(pca.explained_variance_, linewidth=2)
# plt.axis('tight')
# plt.xlabel('n_components')
# plt.ylabel('explained_variance_')
# plt.savefig('PCA_tf-idf.png')


#U,S,V = np.linalg.svd(tfs.A, full_matrices=False)
#print(U.shape, V.shape, S.shape)
#Asvd = np.dot(np.dot(U, np.diag(S)), V)

#print(np.std(tfs.A), np.std(Asvd), np.std(tfs.A - Asvd))


#
#