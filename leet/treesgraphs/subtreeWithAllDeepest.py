# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def dfs(node, d):
            if node:
                l, ln = dfs(node.left, d)
                r, rn = dfs(node.right, d)
                
                if l > r:
                    return l+1, ln
                elif l < r:
                    return r+1, rn
                else:
                    return l+1, node
            else:
                return 0, None
        
        return dfs(root, 0)[1]