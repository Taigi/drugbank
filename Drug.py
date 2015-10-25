__author__ = 'root'
import Classification

class Drug:

    def __init__(self):
        self.primary_id = None
        self.other_ids = []
        self.name = ''
        self.international_brand = ''
        self.description = ''
        self.indication = ''
        self.classification = Classification()

    def __init__(self, primary_id, other_ids, name, international_brand, description, indication, classification=None):
        self.primary_id = primary_id
        self.other_ids = other_ids
        self.name = name
        self.international_brand = international_brand
        self.description = description
        self.indication = indication
        self.classification = classification

    def addClassificaion(self, classification):
        self.classification = classification

    def printout(self):
        print '\n----------------\n'
        print 'Drug:'
        print 'Primary id: ' + self.primary_id
        print 'Other ids: '
        for ids in self.other_ids: print '\t> '+ ids
        print 'Name: ' + self.name
        print 'International brands: '
        print self.international_brand
        print 'Description: ' + self.description
        print 'Indication: ' + self.indication
        self.classification.printout()
        print '\n----------------\n'
