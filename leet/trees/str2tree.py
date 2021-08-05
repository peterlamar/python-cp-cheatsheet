# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if len(s)==0:
            return
        
        stk = [TreeNode()]
        num = ''
        
        s += ')'
        
        for i, c in enumerate(s):
            if c == ')':
                stk.pop()
            elif c != '(':
                num += c
                if i + 1 < len(s) and not s[i+1].isdigit():
                    node = TreeNode(int(num))
                    if stk[-1].left:
                        stk[-1].right = node
                    else:
                        stk[-1].left = node
                    stk.append(node)
                    num = ''
                    
        return stk[0].left