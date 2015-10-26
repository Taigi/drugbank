__author__ = 'root'

from drugBankAcessor_ET import  mapDrugBankFromFile
from sampleDrugBank import sampleFirstNdrugsFromXml, sampleXlinesfromXml
from drugBankDistance import levenshtein_dist

if __name__ == '__main__':

    #for sampling
    # x = 3187
    # path = '/home/iva/DMKM/DrugBank/drugbank.xml'
    # name = 'sampleX.xml'
    # sampleXlinesfromXml(x, path, name)
    # namen = 'sampleN.xml'
    # sampleFirstNdrugsFromXml(4, path, namen)

    #filename = '/home/iva/DMKM/DrugBank/drugbank.xml'
    #filename = '/root/PycharmProjects/drugbank/sampleN.xml'
    filename = '/Volumes/Local/Users/humberto/projects/drugbank/drugbank_short.xml'
    drugs = mapDrugBankFromFile(filename)
    print len(drugs)
    #for key, value in drugs.iteritems():
    #     value.printout()
    d = levenshtein_dist(drugs)
    print d


