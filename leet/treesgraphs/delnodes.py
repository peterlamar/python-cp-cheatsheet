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
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        deleteSet = set(to_delete)
        ans = []
        def dfs(node, root):
            if node:
                if node.val in deleteSet:
                    node.left = dfs(node.left, True)
                    node.right = dfs(node.right, True)
                    return None
                else:
                    node.left = dfs(node.left, False)
                    node.right = dfs(node.right, False)
                    if root:
                        ans.append(node)
                    return node
        dfs(root, True)
        return ans
