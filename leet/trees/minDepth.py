# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time: 3 min
errors: 2nd try
Time: O(n)
Space: O(n) best case, O(log(N)) worst case
"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def helper(node):
            if node is None:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            if node.left and node.right:
                return min(left, right) + 1
            else:
                return max(left, right) + 1
        
        return helper(root)