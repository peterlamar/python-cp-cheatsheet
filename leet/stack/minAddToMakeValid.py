class Solution:
    """
    Track l and r parentheses with seperate counts
    time: O(n)
    space: O(1)
    """
    def minAddToMakeValid(self, s: str) -> int:
        l = r = 0
        
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1
        
        return l + r