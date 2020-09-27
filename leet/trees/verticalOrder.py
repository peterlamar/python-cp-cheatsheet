# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time: nlgn
space: n
"""
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        cols = collections.defaultdict(list)
        
        stk = deque([(root, 0)])
        while stk:
            node , c = stk.popleft()
            if node:
                cols[c].append(node.val)
                stk.append((node.left, c-1))
                stk.append((node.right, c+1))

        return [cols[i] for i in sorted(cols)]