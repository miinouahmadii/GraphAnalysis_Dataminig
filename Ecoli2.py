import networkx as nx
import numpy as np
import math
from matplotlib import pyplot as plt
import random
FileName="Ecoli-directed.txt"

Graphtype=nx.DiGraph()

G = nx.read_edgelist(FileName,nodetype=int)


def pagerank(G):
    d=0.1
    n = G.number_of_nodes()
    A = nx.to_numpy_array(G).T
    
    #sink
    is_sink = np.sum(A, axis=0)==0
    B = (np.ones_like(A) - np.identity(n)) / (n-1)
    A[:, is_sink] += B[:, is_sink]
    
    D_inv = np.diag(1/np.sum(A, axis=0))
    M = np.dot(A, D_inv) 
    
    M = (1-d)*M + d*np.ones((n,n))/n
    
    V = np.ones(n)/n
    for _ in range(100):
        V_last = V
        V = np.dot(M, V)
        if np.sum(np.abs(V-V_last))/n < 0.001:
            return dict(zip(G,V))
              
    return dict(zip(G,V))


prank = pagerank(G)
dic = {k: v for k, v in sorted(prank.items(), key=lambda item: item[1])}
dict_items = dic.items()

first_ten = list(dict_items)[-10:]

print(first_ten)
