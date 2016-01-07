__author__ = 'humberto'

from drugBankLevenshtein import *
from drugBankLSA import *
from drugBankAcessor_ET import *
from sklearn.cluster import AgglomerativeClustering, AffinityPropagation
import numpy

filename = '/Volumes/Local/Users/humberto/projects/drugbank/drugbank.xml'
drugs = mapDrugBankFromFile(filename)
print (len(drugs))

#
ids = sorted(drugs.keys())
ids_dic = dict(enumerate(ids))

print("Total cases ", len(ids))

drug_desc =  drug_term_dictionary(drugs, ids_dic, attr="description")
drug_pharma =  drug_term_dictionary(drugs, ids_dic, attr="pharmacodynamics")
#drug_indication =  drug_term_dictionary(drugs, ids_dic, attr="indication")
drug_name =  drug_term_dictionary(drugs, ids_dic, attr="name")


# Read description
tfidf_desc = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs_desc = tfidf_desc.fit_transform(drug_desc)

# Read pharcacology
tfidf_pharma = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs_pharma = tfidf_pharma.fit_transform(drug_pharma)

# Read indication
#tfidf_indication = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
#tfs_indication = tfidf_indication.fit_transform(drug_indication)


print("Description tf-idf matrix dim: ", tfs_desc.A.shape)
print("Pharmacology tf-idf matrix dim: ", tfs_pharma.A.shape)


# matrix distances
dist_desc = squareform(pdist(tfs_desc.A, cosine))
dist_pharma = squareform(pdist(tfs_pharma.A, cosine))
#dist_indication = squareform(pdist(tfs_indication.A, cosine))
# Name edit distance
dist_name = levenshtein_dist(drug_name)
#idx_desc, idx_pharma = intersection_index(drug_desc.keys(), drug_pharma.keys())

#print(len(idx_desc))
#print(len(idx_pharma))

numpy.save('distMat_desc.npy',dist_desc)
numpy.save('distMat_pharma.npy',dist_pharma)
numpy.save('distMat_name.npy',dist_name)
