# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time: 16 min
errors: none
time: O(N)
space: O(H)
"""
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.total = 0
        def helper(node):
            if node is None:
                return 0
            if L <= node.val <= R:
                self.total += node.val
            if node.val > L:
                left = helper(node.left)  
            if node.val < R:
                right = helper(node.right)
        helper(root)
        return self.total