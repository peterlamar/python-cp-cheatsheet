# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0
        def dfs(node, minval, maxval):
            if not node:
                self.ans = max(self.ans, abs(maxval - minval))
                return
            dfs(node.left, min(node.val, minval), max(node.val, maxval))
            dfs(node.right, min(node.val, minval), max(node.val, maxval))
        dfs(root, float('inf'), float('-inf')
        return self.ans