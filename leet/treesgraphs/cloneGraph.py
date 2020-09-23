"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return
        
        cloneNode = Node(node.val, [])
        ref = {node:cloneNode}
        stk = [node]
        
        while stk:
            n = stk.pop()
            for nei in n.neighbors:
                if nei not in ref:
                    cl = Node(nei.val, [])
                    ref[nei] = cl
                    ref[n].neighbors.append(cl)
                    stk.append(nei)
                else:
                    ref[n].neighbors.append(ref[nei])
        
        return cloneNode
        
        
            