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


dist_desc = numpy.load('distMat_desc.npy')
dist_pharma = numpy.load('distMat_pharma.npy')
dist_name = numpy.load('distMat_name.npy')
dist_atc = numpy.load('dm_uw_atc.npy')
print("Shape desc: ", dist_desc.shape)
print("Shape pharma: ", dist_pharma.shape)
print("Shape name: ", dist_atc.shape)
print("Shape atc: ", dist_atc.shape)
print("Max: ", dist_atc.max())

# Hierarchical clustering
# hca = AgglomerativeClustering(linkage="average",affinity="precomputed", connectivity=None, n_clusters=4)
# hca.fit(0.4*dist_desc + 0.4*dist_pharma + 0.2*dist_name * 1/dist_name.max())
#
# # Print the clusters
# clusters_idx = label_idx(hca.labels_, max(hca.labels_)+1)
# for l in clusters_idx.values():
#     print(l)
#     print(idx_to_id(l, ids_dic))
# print('Number of clusters: ', max(hca.labels_)+1)

#
# # Affinity propagation clustering
apc = AffinityPropagation(affinity="precomputed", damping=.925)
#apc.fit(dist_atc)
apc.fit(0.4*dist_desc + 0.4*dist_pharma + 0.2*dist_name * 1/dist_name.max())

# Print the clusters
clusters_idx = label_idx(apc.labels_, max(apc.labels_)+1)
for l in clusters_idx.values():
    print(l)
    print(idx_to_id(l, ids_dic))

print('Number of clusters: ', max(apc.labels_)+1)





# Plot desc distance vs pharma distance
# x = upper_tri_as_list(dist_desc)
# y = upper_tri_as_list(dist_pharma)
# z = upper_tri_as_list(dist_name)
# w = upper_tri_as_list(dist_indication)

# plt.scatter(x, y, alpha=0.75)
# plt.axis('tight')
# plt.xlabel('description tf-idf cosine distance')
# plt.ylabel('pharmacodynamics tf_idf cosine distance')
# #plt.savefig('desc_vs_pharma.png')
#
#
# plt.scatter(z, x, alpha=0.75)
# plt.axis('tight')
# plt.xlabel('name edit distance')
# plt.ylabel('description tf_idf cosine distance')
# #plt.savefig('name_vs_desc.png')
#
#
# plt.scatter(z, y, alpha=0.75)
# plt.axis('tight')
# plt.xlabel('name edit distance')
# plt.ylabel('pharmacodynamics tf_idf cosine distance')
# #plt.savefig('name_vs_pharma.png')

# plt.scatter(x, w, alpha=0.75)
# plt.axis('tight')
# plt.xlabel('description tf-idf cosine distance')
# plt.ylabel('indication tf-idf cosine distance')
# # plt.savefig('desc_vs_indication.png')
#
# plt.scatter(y, w, alpha=0.75)
# plt.axis('tight')
# plt.xlabel('pharmacodynamics tf-idf cosine distance')
# plt.ylabel('indication tf-idf cosine distance')
#plt.savefig('pharma_vs_indication.png')










#
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