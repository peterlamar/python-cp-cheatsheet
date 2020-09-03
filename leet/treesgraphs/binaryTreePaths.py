# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time: O(N)
space: O(N)
"""
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        rtn = []

        if root is None: return []
        
        stk = [(root, str(root.val))]
        
        while stk:
            node, path = stk.pop()
            
            if node.left is None and node.right is None:
                rtn.append(path)
            
            if node.left:
                stk.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stk.append((node.right, path + "->" + str(node.right.val)))
        
        return rtn