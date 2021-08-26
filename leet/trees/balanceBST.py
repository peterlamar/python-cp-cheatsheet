# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Balance a Binary Search Tree
"""
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorder = []
        
        def getOrder(node):
            if node is None:
                return
            getOrder(node.left)
            self.inorder.append(node.val)
            getOrder(node.right)
    
        # Get inorder treenode ["1,2,3,4"]
        getOrder(root)
        
        # Convert to Tree
        #        2
        #       1 3
        #          4
        def bst(listTree):
            if not listTree:
                return None
            mid = len(listTree) // 2
            root = TreeNode(listTree[mid])
            root.left = bst(listTree[:mid])
            root.right = bst(listTree[mid+1:])
            return root

        return bst(self.inorder)
        
        