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


















# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.colors = frozenset([
            'red',
            'green',
            'blue',
            'orange',
            'yellow',
            'white',
        ])

    def assertGraphColoring(self, graph, colors):
        self.assertGraphHasColors(graph, colors)
        self.assertGraphColorLimit(graph)
        for node in graph:
            self.assertNodeUniqueColor(node)

    def assertGraphHasColors(self, graph, colors):
        for node in graph:
            msg = 'Node %r color %r not in %r' % (node.label, node.color, colors)
            self.assertIn(node.color, colors, msg=msg)

    def assertGraphColorLimit(self, graph):
        max_degree = 0
        colors_found = set()
        for node in graph:
            degree = len(node.neighbors)
            max_degree = max(degree, max_degree)
            colors_found.add(node.color)
        max_colors = max_degree + 1
        used_colors = len(colors_found)
        msg = 'Used %d colors and expected %d at most' % (used_colors, max_colors)
        self.assertLessEqual(used_colors, max_colors, msg=msg)

    def assertNodeUniqueColor(self, node):
        for adjacent in node.neighbors:
            msg = 'Adjacent nodes %r and %r have the same color %r' % (
                node.label,
                adjacent.label,
                node.color,
            )
            self.assertNotEqual(node.color, adjacent.color, msg=msg)

    def test_line_graph(self):
        node_a = GraphNode('a')
        node_b = GraphNode('b')
        node_c = GraphNode('c')
        node_d = GraphNode('d')

        node_a.neighbors.add(node_b)
        node_b.neighbors.add(node_a)
        node_b.neighbors.add(node_c)
        node_c.neighbors.add(node_b)
        node_c.neighbors.add(node_d)
        node_d.neighbors.add(node_c)

        graph = [node_a, node_b, node_c, node_d]
        tampered_colors = list(self.colors)
        color_graph(graph, tampered_colors)
        self.assertGraphColoring(graph, self.colors)

    def test_separate_graph(self):
        node_a = GraphNode('a')
        node_b = GraphNode('b')
        node_c = GraphNode('c')
        node_d = GraphNode('d')

        node_a.neighbors.add(node_b)
        node_b.neighbors.add(node_a)
        node_c.neighbors.add(node_d)
        node_d.neighbors.add(node_c)

        graph = [node_a, node_b, node_c, node_d]
        tampered_colors = list(self.colors)
        color_graph(graph, tampered_colors)
        self.assertGraphColoring(graph, self.colors)

    def test_triangle_graph(self):
        node_a = GraphNode('a')
        node_b = GraphNode('b')
        node_c = GraphNode('c')

        node_a.neighbors.add(node_b)
        node_a.neighbors.add(node_c)
        node_b.neighbors.add(node_a)
        node_b.neighbors.add(node_c)
        node_c.neighbors.add(node_a)
        node_c.neighbors.add(node_b)

        graph = [node_a, node_b, node_c]
        tampered_colors = list(self.colors)
        color_graph(graph, tampered_colors)
        self.assertGraphColoring(graph, self.colors)

    def test_envelope_graph(self):
        node_a = GraphNode('a')
        node_b = GraphNode('b')
        node_c = GraphNode('c')
        node_d = GraphNode('d')
        node_e = GraphNode('e')

        node_a.neighbors.add(node_b)
        node_a.neighbors.add(node_c)
        node_b.neighbors.add(node_a)
        node_b.neighbors.add(node_c)
        node_b.neighbors.add(node_d)
        node_b.neighbors.add(node_e)
        node_c.neighbors.add(node_a)
        node_c.neighbors.add(node_b)
        node_c.neighbors.add(node_d)
        node_c.neighbors.add(node_e)
        node_d.neighbors.add(node_b)
        node_d.neighbors.add(node_c)
        node_d.neighbors.add(node_e)
        node_e.neighbors.add(node_b)
        node_e.neighbors.add(node_c)
        node_e.neighbors.add(node_d)

        graph = [node_a, node_b, node_c, node_d, node_e]
        tampered_colors = list(self.colors)
        color_graph(graph, tampered_colors)
        self.assertGraphColoring(graph, self.colors)

    def test_loop_graph(self):
        node_a = GraphNode('a')

        node_a.neighbors.add(node_a)

        graph = [node_a]
        tampered_colors = list(self.colors)
        with self.assertRaises(Exception):
            color_graph(graph, tampered_colors)


unittest.main(verbosity=2)