__author__ = 'root'

from drugBankAcessor_ET import  mapDrugBankFromFile
from sampleDrugBank import sampleFirstNdrugsFromXml, sampleXlinesfromXml
from drugBankDistance import levenshtein_dist
from ClassificationGraph import buildClassificationGraphfromList, calculateDistMatrix, buildClassificationWeightedGraphfromList, calculateWeightedDistMatrix
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


    # print 'building graph'
    # graph = buildClassificationGraphfromList(drugs.values())
    # print 'building matrix distance'
    # matrix = calculateDistMatrix(graph, drugs.keys())
    # print(matrix)

    # print 'building weighted graph'
    # weighted_graph = buildClassificationWeightedGraphfromList(drugs.values())
    # print 'building weighthed matrix distance'
    # wght_matrix = calculateWeightedDistMatrix(weighted_graph, drugs.keys())
    # print(wght_matrix)


    #for key, value in drugs.iteritems():
    #     value.printout()
    #d = levenshtein_dist(drugs)
    #print d


