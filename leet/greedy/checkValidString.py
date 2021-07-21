"""
( - max = 1, min = 1
(*( max = 3, min = 1
(*)=
valid if min = 0
Time: O(n)
Space: O(1)
"""

class Solution:
    def checkValidString(self, s:str) -> bool:
        cmax = cmin = 0
        for c in s:
            if c == '(':
                cmax = cmax + 1
                cmin = cmin + 1
            elif c == ')':
                cmax = cmax - 1
                cmin = max(cmin-1, 0)
            elif c == '*':
                cmax = cmax + 1
                cmin = max(cmin-1, 0)

            if cmax < 0:
                return False
                
        return cmin == 0
                
        