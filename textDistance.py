__author__ = 'humberto'

from drugBankLevenshtein import *
from drugBankLSA import *
from drugBankAcessor_ET import *
from sklearn.decomposition import TruncatedSVD, PCA
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer, normalize, scale
from sklearn.cluster import AgglomerativeClustering, AffinityPropagation
import numpy

filename = '/Volumes/Local/Users/humberto/projects/drugbank/drugbank.xml'
drugs = mapDrugBankFromFile(filename)
print (len(drugs))


#
ids = sorted(drugs.keys())
ids_dic = dict(enumerate(ids))
total_cases = len(ids)
print("Total cases ", total_cases)

attribute = ['description', 'indication', 'pharmacodynamics']

variable =  drug_term_dictionary(drugs, ids_dic, attr=attribute)

# tf-idf
tfidf_variable = TfidfVectorizer(tokenizer=tokenize, stop_words='english',
                                 ngram_range=(1,1))
tfs_variable = tfidf_variable.fit_transform(variable)

# Dimensionality reduction
print("tf-idf matrix dim: ", tfs_variable.A.shape)
tfs_scale = scale(tfs_variable.A, axis=0, with_std=False)
print("Num vars: ", len(np.mean(tfs_scale, axis=0)))
print('Total variance: ', np.var(tfs_variable.A,axis=0).sum())

svd = TruncatedSVD(n_components=100, random_state=42)
normalizer = Normalizer(copy=False)
lsa = make_pipeline(svd, normalizer)
tfs_red = lsa.fit_transform(tfs_scale)
#numpy.save('./data/tf-idf_reduced100c.npy',tfs_red)

print('Reduced X shape: ', tfs_red.shape)
#print('Explained variance' , svd.explained_variance_ratio_.cumsum())
print('Explained variance' , svd.explained_variance_ratio_.sum())

plt.figure()
plt.plot(svd.explained_variance_ratio_)
plt.axis('tight')
plt.xlabel('num components')
plt.ylabel('explained variance')
#plt.show()
#plt.savefig('./plots/LSAnum_comp.png')

# Distance matrix
dist = squareform(pdist(tfs_scale, 'euclidean'))
dist_red = squareform(pdist(tfs_red, 'euclidean'))
#numpy.save('./data/dist_text.npy',dist)
#numpy.save('./data/dist_text_reduced100c.npy',dist_red)

