import unittest

"""
time: > 20 min
errors: mostly input error
time: O(N + M) graph nodes + edges 
space: O(D+1) colors
"""
class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def color_graph(graph, colors):
    
    for node in graph:
        nc = set()
        for n in node.neighbors:
            nc.add(n.color)
            
        for c in colors:
            if c not in nc:
                node.color = c
                break
        
    return 0