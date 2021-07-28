"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1 = p
        p2 = q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
            
        return p1


    def lowestCommonAncestor(self, p, q):
        pVals = set()
        def traverse_up(root):
            if root == None or root in pVals:
                return root
            pVals.add(root)
            return traverse_up(root.parent)
            
        return traverse_up(p) or traverse_up(q)