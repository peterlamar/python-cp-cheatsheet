# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time: 11min
errors: non
time: O(N)
space: O(H)
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.dif = float('inf')
        self.val = 0
        
        if root:
            self.val = root.val
        else:
            return
        
        def helper(node):
            if node is None:
                return 0

            if node:
                if abs(node.val - target) < self.dif:
                    self.dif = abs(node.val - target)
                    self.val = node.val

                helper(node.left)
                helper(node.right)
            
        helper(root)
        return self.val

    """
    time: 5 min
    time: O(H)
    space: O(1)
    """
    def closestValue2(self, root: TreeNode, target: float) -> int:
        self.dif = float('inf')
        self.val = root.val
        
        node = root
        
        while node:
            if abs(node.val - target) < self.dif:
                self.dif = abs(node.val - target)
                self.val = node.val
            if target < node.val:
                node = node.left
            else:
                node = node.right
        
        return self.val