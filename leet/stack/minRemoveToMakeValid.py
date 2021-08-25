"""
time: > 10 min
time: O(N)
space: O(N)
Minimum Remove to Make Valid Parentheses
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        s = list(s)
        
        # Key insight: Store indexes in stack
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                if stk:
                    stk.pop()
                else:
                    s[i] = ''
        
        while stk:
            s[stk.pop()] = ''
        
        return "".join(s)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rtn = list(s)
        stk = []
        
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                if len(stk) == 0:
                    rtn[i] = ''
                else:
                    stk.pop()
        
        while stk:
            rtn[stk.pop()] = ''
            
        return "".join(rtn)
        