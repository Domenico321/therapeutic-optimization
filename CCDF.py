# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:36:08 2022

@author: Domenico
"""
#This code produce fig. 6 of the report on the basis of the comparison
#made between the network implemented for this research with three types of
#canonical networks through the evaluation of complementary cumulative distribution
#function (CCDF)
from pylab import *
import networkx as nx
n = 131
er = nx.erdos_renyi_graph(n, 0.01)
ws = nx.watts_strogatz_graph(n, 10, 0.01)
ba = nx.barabasi_albert_graph(n, 5)
g = nx.read_adjlist('Adjacency_list.csv', delimiter = ',')

Pk = [float(x) / n for x in nx.degree_histogram(er)]
domain = range(len(Pk))
ccdf = [sum(Pk[k:]) for k in domain]
loglog(domain, ccdf, '-', label = 'Erdos-Renyi')

Pk = [float(x) / n for x in nx.degree_histogram(ws)]
domain = range(len(Pk))
ccdf = [sum(Pk[k:]) for k in domain]
loglog(domain, ccdf, '--', label = 'Watts-Strogatz')

Pk = [float(x) / n for x in nx.degree_histogram(ba)]
domain = range(len(Pk))
ccdf = [sum(Pk[k:]) for k in domain]
loglog(domain, ccdf, ':', label = 'Barabasi-Albert')

Pk = [float(x) / n for x in nx.degree_histogram(g)]
domain = range(len(Pk))
ccdf = [sum(Pk[k:]) for k in domain]
loglog(domain, ccdf, '*', label = 'Network')



xlabel('k')
ylabel('F(k)')
legend()
show()