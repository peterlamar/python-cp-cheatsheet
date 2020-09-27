# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.mx = 0
        def dfs(node):
            if node:
                l = dfs(node.left)
                r = dfs(node.right)
                total = l + r
                self.mx = max(self.mx, total) 
                return max(l, r) + 1
            else:
                return 0
        dfs(root)
        return self.mx