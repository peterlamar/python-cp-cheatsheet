# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        stk = [(root, 0)]
        rtn = []
        while stk:
            node, depth = stk.pop()
            if node:
                if len(rtn) < depth + 1:
                    rtn.append([])
                rtn[depth].append(node.val)                
                stk.append((node.right, depth+1))
                stk.append((node.left, depth+1))
                
        return rtn