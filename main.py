__author__ = 'root'

from drugBankAcessor_ET import  mapDrugBankFromFile
from sampleDrugBank import sampleFirstNdrugsFromXml, sampleXlinesfromXml
from drugBankDistance import levenshtein_dist
from ClassificationGraph import buildClassificationGraphfromList
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':

    #for sampling
    # x = 3187
    # path = '/home/iva/DMKM/DrugBank/drugbank.xml'
    # name = 'sampleX.xml'
    # sampleXlinesfromXml(x, path, name)
    # namen = 'sampleN.xml'
    # sampleFirstNdrugsFromXml(4, path, namen)

    #filename = '/home/iva/DMKM/DrugBank/drugbank.xml'
    filename = '/root/PycharmProjects/drugbank/sampleN.xml'
    #filename = '/Volumes/Local/Users/humberto/projects/drugbank/drugbank_short.xml'
    drugs = mapDrugBankFromFile(filename)
    # for drug in drugs.values():
    #     drug.printout()
    print len(drugs)
    graph = buildClassificationGraphfromList(drugs.values())
    nx.draw_networkx(graph, arrows=True, with_labels=True)
    # G=nx.dodecahedral_graph()
    # nx.draw(G)
    # nx.draw(G,pos=nx.spring_layout(G))
    plt.show()
    #for key, value in drugs.iteritems():
    #     value.printout()
    #d = levenshtein_dist(drugs)
    #print d


