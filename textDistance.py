__author__ = 'humberto'

from drugBankLevenshtein import *
from drugBankLSA import *
from drugBankAcessor_ET import *

filename = '/Volumes/Local/Users/humberto/projects/drugbank/drugbank_short.xml'
drugs = mapDrugBankFromFile(filename)


#
ids = sorted(drugs.keys())
ids_dic = dict(enumerate(ids))

drug_desc =  drug_term_dictionary(drugs, ids_dic, attr="description")
drug_pharma =  drug_term_dictionary(drugs, ids_dic, attr="pharmacodynamics")
drug_name =  drug_term_dictionary(drugs, ids_dic, attr="name")



# Read description
tfidf_desc = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs_desc = tfidf_desc.fit_transform(drug_desc)

# Read pharcacology
tfidf_pharma = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs_pharma = tfidf_pharma.fit_transform(drug_pharma)

print("Description tf-idf matrix dim: ", tfs_desc.A.shape)
print("Pharmacology tf-idf matrix dim: ", tfs_pharma.A.shape)

# matrix distances
dist_desc = squareform(pdist(tfs_desc.A, cosine))
dist_pharma = squareform(pdist(tfs_pharma.A, cosine))
# Name edit distance
dist_name = levenshtein_dist(drug_name)
#idx_desc, idx_pharma = intersection_index(drug_desc.keys(), drug_pharma.keys())

#print(len(idx_desc))
#print(len(idx_pharma))

# Plot desc distance vs pharma distance
x = upper_tri_as_list(dist_desc)
y = upper_tri_as_list(dist_pharma)
z = upper_tri_as_list(dist_name)


plt.scatter(x, y, alpha=0.75)
plt.axis('tight')
plt.xlabel('description tf-idf cosine distance')
plt.ylabel('pharmacodynamics tf_idf cosine distance')
plt.savefig('desc_vs_pharma.png')


plt.scatter(z, x, alpha=0.75)
plt.axis('tight')
plt.xlabel('name edit distance')
plt.ylabel('description tf_idf cosine distance')
plt.savefig('name_vs_desc.png')


plt.scatter(z, y, alpha=0.75)
plt.axis('tight')
plt.xlabel('name edit distance')
plt.ylabel('pharmacodynamics tf_idf cosine distance')
plt.savefig('name_vs_pharma.png')

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