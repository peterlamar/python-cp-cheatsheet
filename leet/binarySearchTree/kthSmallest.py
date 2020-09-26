# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time: 20 min

error: forgot 'else' clause
off by one with count
"""
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stk = [(root, False)]
        cnt = 1

        while stk:
            node, visited = stk.pop()
            if node:
                if visited:
                    if k == cnt:
                        return node.val
                    else:
                        cnt += 1
                else:
                    stk.append((node.right, False))
                    stk.append((node, True))
                    stk.append((node.left, False))
        
        return -1
                