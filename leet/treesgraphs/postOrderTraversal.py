# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Post order = l, r, root
"""
        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            print(node.val, end=' ')
        postorder(root)
"""
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        rtn = []
        stk = [(root, False)]
        while stk:
            node, visited = stk.pop()
            if node:
                if visited:
                    rtn.append(node.val)
                else:
                    stk.append((node, True))
                    stk.append((node.right, False))
                    stk.append((node.left, False))

        return rtn
