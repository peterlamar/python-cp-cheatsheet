# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time:n
space: n
"""
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        
        def dfs(node, d):
            if node:
                if len(ans) == d:
                    ans.append([0,0])
                ans[d][0] += node.val 
                ans[d][1] += 1
                dfs(node.left, d+1)
                dfs(node.right, d+1)
        
        dfs(root, 0)
        
        return [s/n for s,n in ans]