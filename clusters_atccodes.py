import pickle
from drugBankAcessor_ET import mapDrugBankFromFile
import matplotlib.pyplot as plt
# import numpy as np
# import pandas
from collections import Counter

##### this chunk of code goes to textClustering.py to save the dictionary that we read here
# output = open('./data/clusters_dbid.pkl', 'wb')
# pickle.dump(clusters_dbid, output)
# output.close()



filename = '/home/iva/DMKM/DrugBank/drugbank.xml'
drugs = mapDrugBankFromFile(filename)

pkl_file = open('./data/clusters_dbid.pkl', 'rb')
clusters_dbid = pickle.load(pkl_file)
pkl_file.close()

cols_rgb = [(240,163,255),(0,117,220),(153,63,0),(76,0,92),(25,25,25),(0,92,49),(43,206,72),
            (255,204,153),(128,128,128),(148,255,181),(143,124,0),(157,204,0),(194,0,136),
            (0,51,128),(255,164,5),(255,168,187),(66,102,0),(255,0,16),(94,241,242),(0,153,143),
            (224,255,102),(116,10,255),(153,0,0),(255,255,128),(255,255,0),(255,80,5)]
cols_hex = ['#%02x%02x%02x' % x for x in cols_rgb]


for cluster, ids in clusters_dbid.iteritems():
    print('Cluster number: ' + str(cluster))
    all_atc_codes = [drugs[id].atc_codes for id in ids]
    atc_codes3 = [atc[0:3] for atccodes in all_atc_codes for atc in atccodes]
    print(atc_codes3)
    atc_counts = Counter(atc_codes3)
    sortedatc = sorted(atc_counts.keys())
    sortedvalues = [atc_counts[key] for key in sortedatc]
    indexes = xrange(0,len(atc_counts))
    plt.bar(indexes, sortedvalues,width=1 ,color=cols_hex[cluster])
    ticksindexes = [indexes[i]+0.5 for i in indexes]
    plt.xticks(ticksindexes, sortedatc)
    # df = pandas.DataFrame.from_dict(atc_counts, orient='index')
    # df.plot(kind='bar', color=cols_hex[cluster], sort_columns = True, legend= False)
    plt.title("ATC code Histogram Cluster " + `cluster` )
    plt.savefig('./plots/histo'+`cluster`+'.png')
    plt.close()
    # plt.show()