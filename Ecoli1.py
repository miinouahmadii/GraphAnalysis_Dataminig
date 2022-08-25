import networkx as nx
import numpy as np
import math
from matplotlib import pyplot as plt
import random

FileName="Ecoli.txt"

Graphtype=nx.Graph()

G = nx.read_edgelist(FileName,nodetype=int)

def diameter (G):
    order = G.order()
    e = {}
    for n in G.nodes():
        length = nx.single_source_shortest_path_length(G, n)
        L = len(length)
        e[n] = max(length.values())
    
    return max(e.values())

print (diameter(G))

######################

def plot_degree_distribution(G):
    degrees = {}
    for n in G.nodes():
        deg = G.degree(n)
        if deg not in degrees:
            degrees[deg] = 0
        degrees[deg] += 1
        
    order = G.order()

    items = sorted(degrees.items())
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([k for (k, v) in items], [v for (k, v) in items],'b-')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.show()

plot_degree_distribution(G)

##############################33

def plot_degree_probability (G):
    k = []
    Pk = []
    logk=[]
    logPk=[]

    for node in list(G.nodes()):
        degree = G.degree(nbunch=node)
        try:
            pos = k.index(degree)
        except ValueError as e:
            k.append(degree)
            Pk.append(1)
    else:
        Pk[pos] += 1

    for i in range(len(k)):
        logk.append(math.log10(k[i]))
        logPk.append(math.log10(Pk[i]))

    order = np.argsort(logk)
    logk_array = np.array(logk)[order]
    logPk_array = np.array(logPk)[order]
    plt.plot(logk_array, logPk_array, ".")
    m, c = np.polyfit(logk_array, logPk_array, 1)
    plt.plot(logk_array, m*logk_array + c, "-")
    
plot_degree_probability(G)

########################3
def clustering_coeff(G):
    nodes= nodes_nbrs = G.adj.items()
    
    triangles=0
    triads = list()
    for v,v_numbers in nodes:
        vs=set(v_numbers)-set([v])
        triads.append(len(vs))
        for w in vs:
            ws=set(G[w])-set([w])
            triangles+=len(vs.intersection(ws))
    
    cont = sum(d*(d-1) for d in triads)
    
    return triangles / cont
    
print(clustering_coeff(G))

#################################
