# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# https://en.wikipedia.org/wiki/Timsort  
# identifies the two already sorted runs as such and simply merges them
# sorts are done in C
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stk1 = []
        stk2 = []
        
        def dfs(node, stk):
            if node is None:
                return
            dfs(node.left, stk)
            stk.append(node.val)
            dfs(node.right, stk)
            
        dfs(root1, stk1)
        dfs(root2, stk2)
        
        return sorted(stk1 + stk2)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stk1 = []
        stk2 = []
        
        def dfs(node, stk):
            if node is None:
                return
            dfs(node.left, stk)
            stk.append(node.val)
            dfs(node.right, stk)
            
        dfs(root1, stk1)
        dfs(root2, stk2)
        
        s0 = s1 = 0
        rtn = []
        
        while s0 < len(stk1) and s1 < len(stk2):
            if stk1[s0] < stk2[s1]:
                rtn.append(stk1[s0])
                s0 += 1
            else:
                rtn.append(stk2[s1])
                s1 += 1
        
        return rtn + stk1[s0:] + stk2[s1:]