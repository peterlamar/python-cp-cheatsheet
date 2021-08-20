# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time: 2 min
errors: lots of syntax, need to practice recursion
Time: O(n)
Space: O(n) worst case, best case O(log(N)) because its 
only going down one leg at a time
    3
   / \
  9  20
    /  \
   15   7
   
9->15->7->20->3   
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(node):
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            return max(left, right) + 1
            
        return helper(root)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def bfs(node):
            if node is not None:
                rtn = {}
                for i, c in enumerate(node.children):
                    rtn[i] = bfs(c)
                
                m = 0
                for k in rtn:
                    m = max(m, rtn[k])
                return m + 1
            else:
                return 0
            
        return bfs(root)