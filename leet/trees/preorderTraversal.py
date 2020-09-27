# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
        
"""
        self.rtn = []
        def preorder(node):
            if node is None:
                return
            self.rtn.append(node.val)
            print(node.val, end=' ')
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return self.rtn
"""
"""
time: 5 min
errors: missed right/left flip from adding to return
missed empty edge case
"""
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        rtn = []
        stk = [root]
        while stk:
            node = stk.pop()
            if node:
                rtn.append(node.val)
                stk.append(node.right)
                stk.append(node.left)

        return rtn