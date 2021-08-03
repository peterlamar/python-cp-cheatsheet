# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time: N
space: N worst case (logN if balanced)
"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.cnt = 0
        
        def dfs(node):
            if node is None:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            self.cnt = max(self.cnt, l+r)
            
            return max(l, r) + 1
        
        dfs(root)
        
        return self.cnt