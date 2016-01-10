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

ncomp = '200'
mat = numpy.load('./data/tf-idf_reduced'+ncomp+'c.npy')
dist = numpy.load('./data/dist_text.npy')
dist_red = numpy.load('./data/dist_text_reduced'+ncomp+'c.npy')

#
hca = AgglomerativeClustering(linkage="ward",affinity="euclidean", connectivity=None, n_clusters=14)
hca.fit(mat)
nclust = max(hca.labels_)+1

# Print the clusters
clusters_idx = label_idx(hca.labels_, nclust)
clusters_dbid = dict()
for l in clusters_idx.keys():
     clusters_dbid[l] = idx_to_id(clusters_idx[l], ids_dic)
print('Number of clusters: ', max(hca.labels_)+1)
print('Clusters:\n ', clusters_dbid)


############ Visual evaluation
fig = plt.figure()
plt.imshow(dist, interpolation='nearest', vmin=0, vmax=1.4)
plt.colorbar().set_label('Distance')
plt.show()
#plt.savefig('./plots/LSAnum_comp.png')

fig = plt.figure()
plt.imshow(dist_red, interpolation='nearest', vmin=0, vmax=1.4)
plt.colorbar()
plt.show()

# Order the distance matrices according to clusters
clusters_idx_ordered = list()
for i in range(nclust):
    clusters_idx_ordered += clusters_idx[i]

print((dist_red[:, clusters_idx_ordered][clusters_idx_ordered]/dist_red[:, clusters_idx_ordered][clusters_idx_ordered].max()).max())

fig = plt.figure()
plt.imshow(dist_red[:, clusters_idx_ordered][clusters_idx_ordered],
           interpolation='nearest', vmin=0, vmax=1.4)
plt.colorbar().set_label('Distance')
plt.show()

fig = plt.figure()
plt.imshow(dist[:, clusters_idx_ordered][clusters_idx_ordered],
           interpolation='nearest', vmin=0, vmax=1.4)
plt.colorbar().set_label('Distance')
plt.show()



################
# Motivacion
# Descripcion drugbank
# Intro
# Evaluacion (analisis de errores)
# Analisis futuro

# Plot dist numero de elementos
# Medioides
# Diametro / dist clusters

# junta martes 19 en la UB despues de las 14
# Miercoles o jueves en UPC a cualquier hora



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


