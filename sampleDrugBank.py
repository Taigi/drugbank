__author__ = 'root'

# script to sample first x lines of drugbank.xml


def sampleXlinesfromXml(x, path, name):
    file = open(path,'r')
    fout = open(name, 'w')
    for i in xrange(0,x):
        line = file.readline()
        fout.write(line)
    fout.write('</drugbank>') # end tag
    file.close()
    fout.close()

# potentially unsafe, use at your own risk ;)
def sampleFirstNdrugsFromXml(n, path,name):
    file = open(path,'r')
    fout = open(name, 'w')
    i = 0
    while (i < n):
        line = file.readline()
        fout.write(line)
        print line
        if line == "</drug>\n":
            i+=1
    fout.write('</drugbank>') # end tag
    file.close()
    fout.close()


# x = 3187
# path = '/home/iva/DMKM/DrugBank/drugbank.xml'
# name = 'sampleN.xml'
#sampleXlinesfromXml(x, path, name)
#sampleFirstNdrugsFromXml(4, path, name)