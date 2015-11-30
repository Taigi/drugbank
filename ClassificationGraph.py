import networkx as nx
import numpy
from Classification import Classification

def buildGraphfromList(drugs):
    dir_graph = nx.DiGraph()
    for drug in drugs:
        cls = drug.classification
        if cls != None:
            dir_graph.add_node(drug.primary_id)
            dir_graph.add_node(cls.direct_parent)
            dir_graph.add_edge(cls.direct_parent,drug.primary_id)
            dir_graph.add_node(cls.superclass)
            dir_graph.add_node(cls.class_type)
            dir_graph.add_node(cls.subclass)
            dir_graph.add_edge(cls.superclass,drug.primary_id)
            dir_graph.add_edge(drug.name,cls.subclass)
    return dir_graph


#undirected
def buildClassificationGraphfromList(drugs):
    graph = nx.Graph()
    for drug in drugs:
        cls = drug.classification
        if cls != None:
            graph.add_node(cls.kingdom)
            graph.add_node(cls.superclass)
            graph.add_edge(cls.kingdom, cls.superclass)

            graph.add_node(cls.class_type)
            graph.add_edge(cls.superclass, cls.class_type)

            graph.add_node(cls.subclass)
            graph.add_edge(cls.class_type, cls.subclass)

            if (cls.direct_parent!=cls.subclass):
                graph.add_node(cls.direct_parent)
                graph.add_edge(cls.subclass, cls.direct_parent)

            graph.add_node(drug.primary_id)
            graph.add_edge(cls.direct_parent, drug.primary_id)
    return graph


def calculateDistMatrix(graph, drugids):
    n = len(drugids)
    graph_distance = numpy.zeros(shape=(n,n))

    sortedids = sorted(drugids)
    for i in xrange(n):
        for j in xrange(i+1,n):
            try:
                shortest_path = nx.shortest_path_length(graph, sortedids[i], sortedids[j])
            except nx.NetworkXNoPath:
                shortest_path = -1
            except nx.NetworkXError:
                shortest_path = -1
            graph_distance[i,j] = shortest_path
        print i
    return graph_distance

def buildClassificationWeightedGraphfromList(drugs):
    graph = nx.Graph()
    for drug in drugs:
        cls = drug.classification
        if cls != None:
            graph.add_node(cls.kingdom)
            graph.add_node(cls.superclass)
            graph.add_edge(cls.kingdom, cls.superclass, weight=100)

            graph.add_node(cls.class_type)
            graph.add_edge(cls.superclass, cls.class_type,weight=50)

            graph.add_node(cls.subclass)
            graph.add_edge(cls.class_type, cls.subclass,weight=15)

            if (cls.direct_parent!=cls.subclass):
                graph.add_node(cls.direct_parent)
                graph.add_edge(cls.subclass, cls.direct_parent,weight=10)

            graph.add_node(drug.primary_id)
            graph.add_edge(cls.direct_parent, drug.primary_id)
    return graph
def calculateWeightedDistMatrix(graph, drugids):
    n = len(drugids)
    graph_distance = numpy.zeros(shape=(n,n))

    sortedids = sorted(drugids)
    for i in xrange(n):
        for j in xrange(i+1,n):
            try:
                shortest_path = nx.dijkstra_path_length(graph, sortedids[i], sortedids[j])
            except nx.NetworkXNoPath:
                shortest_path = -1
            except nx.NetworkXError:
                shortest_path = -1
            graph_distance[i,j] = shortest_path
        print i
    return graph_distance

    #nx.draw_networkx(graph, arrows=True, with_labels=True)
    # G=nx.dodecahedral_graph()
    # nx.draw(G)
    # nx.draw(G,pos=nx.spring_layout(G))


    # print 'building graph'
    # graph = buildClassificationGraphfromList(drugs.values())
    # print 'building matrix distance'
    # matrix = calculateDistMatrix(graph, drugs.keys())
    # print(matrix)

    # print 'building weighted graph'
    # weighted_graph = buildClassificationWeightedGraphfromList(drugs.values())
    # # print 'building weighthed matrix distance'
    # # wght_matrix = calculateWeightedDistMatrix(weighted_graph, drugs.keys())
    # # print(wght_matrix)
    #
    # drug  = sorted(drugs.keys())[len(drugs)-1]
    # hm = drugs[drug]
    # hm.printout()
    #
    # drug1  = sorted(drugs.keys())[1]
    # hm = drugs[drug1]
    # hm.printout()
    # pth = nx.dijkstra_path(weighted_graph, drug1, drug)
    # ln = nx.dijkstra_path_length(weighted_graph, drug1, drug)
    # print(pth)
    # print(ln)


    # with open('shotest_dist_drugbank', 'w') as f:
    #     numpy.save(f, matrix)
    # with open('dist300', 'r') as f:
    #     matrix2 = numpy.load(f)
    # print(matrix2)
