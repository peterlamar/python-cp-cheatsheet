# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        st = set()
        stk = [root]
        
        while stk:
            node = stk.pop()
            if node:
                if node.val in st:
                    return True
                else:
                    st.add(k - node.val)
                stk.append(node.left)
                stk.append(node.right)

        return False