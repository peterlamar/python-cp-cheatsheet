# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stk = []
        self.node = root
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.node:
            self.stk.append(self.node)
            self.node = self.node.left 
        nxt = self.stk.pop()
        self.node = nxt.right 
        return nxt.val 

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stk or self.node:
            return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()