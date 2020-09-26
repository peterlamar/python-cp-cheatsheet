# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        self.total = 0
        self.mx = float('-inf')
        def dfs(node, cnt):
            if node:
                self.total += 1
                self.mx = max(self.mx, cnt)
                dfs(node.left, (cnt*2))
                dfs(node.right, (cnt*2)+1)
        dfs(root, 1)
        return self.total == self.mx
