__author__ = 'root'

# script to sample first x lines of drugbank.xml

x = 3187
path = '/home/iva/DMKM/DrugBank/drugbank.xml'
name = 'sample.xml'
file = open(path,'r')
fout = open(name, 'w')
for i in xrange(0,x):
    line = file.readline()
    fout.write(line)
fout.write('</drugbank>') # end tag
file.close()
fout.close()