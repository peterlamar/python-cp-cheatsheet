# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Error
max(leftMax + rightMax), not  max(leftMax, rightMax) 

https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/674181/Python-recursive-and-iterative-solution-(easy-to-read-and-understand)
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
        
            
            
    def maxPathSum(self, root: TreeNode) -> int:
        # Get max of left, right + val
        self.mxPath = float('-inf')

        def dfs(node):
            if node is None:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.mxPath = max(self.mxPath, node.val + left + right)
            return node.val + max(left, right)
        
        dfs(root)
        
        return self.mxPath