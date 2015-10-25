__author__ = 'root'

class DrugBank:

    def __init__(self):
        self.drug_dict = {}

    def __init__(self, dict):
        self.drug_dict = dict

    def addDrug(self, drug):
        self.drug_dict[drug.primary_id] = drug

    def getDrug(self, primary_id):
        return self.drug_dict.get(primary_id)
