# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time: n
space: n
"""
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rtn = []
        
        def dfs(node, d):
            if node:
                if len(rtn) == d:
                    rtn.append(node.val)
                dfs(node.right, d+1)
                dfs(node.left, d+1)
        dfs(root, 0)
        
        return rtn

            