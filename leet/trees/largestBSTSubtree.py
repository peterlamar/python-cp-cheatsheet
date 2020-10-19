# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, float("inf"), float("-inf")
            
            ln, lmin, lmax = dfs(node.left)
            rn, rmin, rmax = dfs(node.right)
            
            if lmax < node.val < rmin:
                return ln + rn + 1, min(lmin, node.val), max(rmax, node.val)
            else:
                return max(ln, rn), float("-inf"), float("inf")
        
        return dfs(root)[0]