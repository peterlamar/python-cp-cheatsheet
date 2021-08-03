# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.foundSum = False
        
        def dfs(node, tmpSum):
            if node is None:
                return 0
            
            tmpSum += node.val

            if node.left is None and node.right is None:
                if tmpSum == targetSum:
                    self.foundSum = True
            
            dfs(node.left, tmpSum)
            dfs(node.right, tmpSum)
            
            
        dfs(root, 0)
        
        return self.foundSum