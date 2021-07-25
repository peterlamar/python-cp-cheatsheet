"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        dummy = Node(0)
        prev = dummy
        
        stk = [(root, False)]
        
        while stk:
            node, visited = stk.pop()
            if node:
                if visited:
                    prev.right = node
                    node.left = prev
                    prev = node       
                else:                
                    if node.right:
                        stk.append((node.right, False))
                    stk.append((node, True))
                    if node.left:
                        stk.append((node.left, False))
        
        node.right = dummy.right
        dummy.right.left = node
        
        return dummy.right

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return
        
        dummy = Node(-1)
        prev = dummy
        
        def inorder(node):
            nonlocal prev
            if node:
                inorder(node.left)
                prev.right = node
                node.left = prev
                prev = node
                inorder(node.right)
                
        inorder(root)
        
        dummy.right.left = prev
        prev.right = dummy.right
        
        return dummy.right
        