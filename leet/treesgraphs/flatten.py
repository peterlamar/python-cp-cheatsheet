# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

Morris Traversal
     5 
    /  \
  2     1
   \   / \ 
   6  10  11
   / 
 44
  \
   23
   
   
      5 
       \
        2
         \
          6
        /  \
      44    1
       \    / \ 
      23   10  11
    
 
      5 
       \
        2
         \
          6
          \ 
           44
            \
            23
             \
              1
             / \ 
            10  11
            
    1
   / \
  2   5
 / \   \
3   4   6      
            
    1
     \
      2   
     / \   
    3   4 
         \
         5
          \
           6
            
"""
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Get rightmostgrandchild
        # change left child to right child
        # attach former right child to rightmostgrandchild
        if not root:
            return None
        
        node = root
        
        while node:
        
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right 
                rightmost.right = node.right 
                node.right = node.left
                node.left = None 
            node = node.right 
        