# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def maxTree(node):
            if node is None:
                return 0
            left = maxTree(node.left)
            right = maxTree(node.right)
            
            if abs(left - right) > 1 or left == -1 or right == -1:
                return -1
            
            return max(left, right) + 1
        
        return maxTree(root) != -1
            