class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        l = r = 0
        for c in S:
            if c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
            elif c == '(':
                l += 1
        return l + r