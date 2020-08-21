# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Error
max(leftMax + rightMax), not  max(leftMax, rightMax) 
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.maxSum = float('-inf')
        self.maxPath(root)
        return self.maxSum

    def maxPath(self, node):
            
        if node is None:
            return 0

        leftMax = max(self.maxPath(node.left), 0)
        rightMax = max(self.maxPath(node.right),0)

        self.maxSum = max(self.maxSum, node.val + leftMax + rightMax)
        
        # See if this is the new max root node
        return max(leftMax, rightMax) + node.val
        
            
            
            