# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stk = [(root, float(-inf), float(inf))]
        while stk:
            node, floor, ceil = stk.pop()
            if node:
                if node.val >= ceil or node.val <= floor:
                    return False
                stk.append((node.right, node.val, ceil))
                stk.append((node.left, floor, node.val))

        return True
        