import networkx as nx
import numpy
from Classification import Classification

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
    dict_sortedids = dict(enumerate(sortedids))
    for i in xrange(n):
        for j in xrange(i+1,n):
            try:
                shortest_path = nx.shortest_path_length(graph, dict_sortedids[i], dict_sortedids[j])
            except nx.NetworkXNoPath:
                shortest_path = -1
            except nx.NetworkXError:
                shortest_path = -1
            graph_distance[i,j] = shortest_path
        print i
    return graph_distance


def buildClassificationWeightedGraphfromList(drugs, weights=[1,10,20,25,50]):
    graph = nx.Graph()
    for drug in drugs:
        cls = drug.classification
        if cls != None:
            graph.add_node(cls.kingdom)
            graph.add_node(cls.superclass)
            graph.add_edge(cls.kingdom, cls.superclass, weight=weights[4])

            graph.add_node(cls.class_type)
            graph.add_edge(cls.superclass, cls.class_type,weight=weights[3])

            graph.add_node(cls.subclass)
            graph.add_edge(cls.class_type, cls.subclass,weight=weights[2])

            if (cls.direct_parent!=cls.subclass):
                graph.add_node(cls.direct_parent)
                graph.add_edge(cls.subclass, cls.direct_parent,weight=weights[1])

            graph.add_node(drug.primary_id)
            graph.add_edge(cls.direct_parent, drug.primary_id, weight=weights[0])
    return graph


def calculateWeightedDistMatrix(graph, drugids):
    n = len(drugids)
    graph_distance = numpy.zeros(shape=(n,n))

    sortedids = sorted(drugids)
    dict_sortedids = dict(enumerate(sortedids))
    for i in xrange(n):
        for j in xrange(i+1,n):
            try:
                shortest_path = nx.dijkstra_path_length(graph, dict_sortedids[i], dict_sortedids[j])
            except nx.NetworkXNoPath:
                shortest_path = -1
            except nx.NetworkXError:
                shortest_path = -1
            graph_distance[i,j] = shortest_path
        print i
    return graph_distance


    #undirected
def buildATCGraphfromList(drugs):
    graph = nx.Graph()
    for drug in drugs:
        codes = drug.atc_codes
        if codes != []:
            for code in codes:
                first = code[0:1]
                second = code[0:3]
                third = code[0:4]
                fourth =code[0:5]
                fifth = code

                graph.add_node(fifth)
                graph.add_node(fourth)
                graph.add_edge(fifth, fourth)

                graph.add_node(third)
                graph.add_edge(fourth, fifth)

                graph.add_node(second)
                graph.add_edge(third, second)

                graph.add_node(first)
                graph.add_edge(second, first)

                graph.add_node(drug.primary_id)
                graph.add_edge(first, drug.primary_id)
    return graph


    def buildATCWeightedGraphfromList(drugs,  weights=[1,10,20,25,50]):
        graph = nx.Graph()
        for drug in drugs:
            codes = drug.atc_codes
            if codes != []:
                for code in codes:
                    first = code[0:1]
                    second = code[0:3]
                    third = code[0:4]
                    fourth =code[0:5]
                    fifth = code

                    graph.add_node(fifth)
                    graph.add_node(fourth)
                    graph.add_edge(fifth, fourth, weight=weights[4])

                    graph.add_node(third)
                    graph.add_edge(fourth, fifth, weight=weights[3])

                    graph.add_node(second)
                    graph.add_edge(third, second, weight=weights[2])

                    graph.add_node(first)
                    graph.add_edge(second, first, weight=weights[1])

                    graph.add_node(drug.primary_id)
                    graph.add_edge(first, drug.primary_id,  weight=weights[0])
        return graph

    #nx.draw_networkx(graph, arrows=True, with_labels=True)
    # G=nx.dodecahedral_graph()
    # nx.draw(G)
    # nx.draw(G,pos=nx.spring_layout(G))
    # plt.show()


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

    # print 'building atc graph'
    # graph = buildATCGraphfromList(drugs.values())
    # test = nx.shortest_path_length(graph, 'A','A01')
    # nx.draw_networkx(graph, arrows=False, with_labels=False)
    # G=nx.dodecahedral_graph()
    # nx.draw(G)
    # nx.draw(G,pos=nx.spring_layout(G))
    # plt.show()
    # print 'building matrix distance'
    # matrix = calculateDistMatrix(graph, drugs.keys())
    # print(matrix)
