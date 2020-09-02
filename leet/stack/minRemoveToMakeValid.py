"""
time: > 10 min
time: O(N)
space: O(N)
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rtn = list(s)
        stk = []
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                if len(stk) > 0:
                    stk.pop()
                else:
                    rtn[i] = ''
        while stk:
            rtn[stk.pop()] = ''
        return "".join(rtn)
            