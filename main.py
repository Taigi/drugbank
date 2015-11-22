__author__ = 'root'

from drugBankAcessor_ET import  mapDrugBankFromFile
from sampleDrugBank import sampleFirstNdrugsFromXml, sampleXlinesfromXml
from drugBankDistance import levenshtein_dist
from ClassificationGraph import buildClassificationGraphfromList, buildGraphfromList
import numpy
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
    filename = '/root/PycharmProjects/drugbank/sample300.xml'
    #filename = '/Volumes/Local/Users/humberto/projects/drugbank/drugbank_short.xml'
    drugs = mapDrugBankFromFile(filename)
    # for drug in drugs.values():
    #     drug.printout()
    print len(drugs)
    graph = buildGraphfromList(drugs.values())
    #graph = buildClassificationGraphfromList(drugs.values())
    graph_distance = dict()
    for drug1, value1 in drugs.iteritems():
        for drug2, value2 in drugs.iteritems():
            # if drug1 == 'DB05103' or drug2 == 'DB05103':
            #     drugs[drug1].printout()
            #     drugs[drug2].printout()
            if (value1 != None and value2 != None and drug1 != drug2):
                try:
                    shortest_path = nx.shortest_path(graph, drug1, drug2)
                except nx.NetworkXNoPath:
                    shortest_path = -1
                except nx.NetworkXError:
                    shortest_path = -1

                graph_distance[(drug1,drug2)] = shortest_path
    for key, value in graph_distance.iteritems():
        if value!= -1:
            print(graph_distance)

    #nx.draw_networkx(graph, arrows=True, with_labels=True)
    # G=nx.dodecahedral_graph()
    # nx.draw(G)
    # nx.draw(G,pos=nx.spring_layout(G))
    #plt.show()
    #for key, value in drugs.iteritems():
    #     value.printout()
    #d = levenshtein_dist(drugs)
    #print d


