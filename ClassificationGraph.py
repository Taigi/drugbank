import networkx as nx
from Classification import Classification

def buildGraphfromList(drugs):
    dir_graph = nx.DiGraph()
    for drug in drugs:
        cls = drug.classification
        if cls != None:
            dir_graph.add_node(drug.name)
            dir_graph.add_node(cls.direct_parent)
            dir_graph.add_edge(cls.direct_parent,drug.name)
            dir_graph.add_node(cls.superclass)
            dir_graph.add_node(cls.subclass)
            dir_graph.add_edge(cls.superclass,drug.name)
            dir_graph.add_edge(drug.name,cls.subclass)
    return dir_graph

def buildClassificationGraphfromList(drugs):
    dir_graph = nx.DiGraph()
    for drug in drugs:
        cls = drug.classification
        if cls != None:
            #dir_graph.add_node(drug.name)
            dir_graph.add_node(cls.direct_parent)
            #dir_graph.add_edge(cls.direct_parent,drug.name)
            dir_graph.add_node(cls.superclass)
            dir_graph.add_node(cls.subclass)
            #dir_graph.add_edge(cls.superclass,drug.name)
            #dir_graph.add_edge(drug.name,cls.subclass)
            dir_graph.add_edge(cls.superclass,cls.subclass)
    return dir_graph