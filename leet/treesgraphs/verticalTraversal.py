# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time: n3lgn
space: n*2
"""
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ans = collections.defaultdict(list)
        
        def dfs(node, c, d):
            if node:
                dfs(node.left, c-1, d+1)
                ans[c].append((node.val,d))
                dfs(node.right, c+1, d+1)

        dfs(root, 0, 0)

        out = []
        for key, value in sorted(ans.items()):
            level = []
            for a,b in sorted(value, key=lambda x: (x[1], x[0])):
                level.append(a)
            out.append(level)
        return out