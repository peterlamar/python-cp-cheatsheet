# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.rtn = 0
        
        def test(node, target):
            if node is None:
                return 0
            
            target -= node.val 
            if target == 0:
                self.rtn += 1
            test(node.left, target)
            test(node.right, target)
        
        def dfs(node):
            if node is None:
                return 0
            
            test(node, targetSum)
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        return self.rtn