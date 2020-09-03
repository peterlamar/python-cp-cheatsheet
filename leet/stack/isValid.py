class Solution:
    def isValid(self, s: str) -> bool:
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]','').replace('()','').replace('{}','')
        return len(s) == 0


"""
time: 10 min
time: O(n)
space: O(n)
errors:
lower case values/keys
Have to use stack because 3 charactors open/close
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mp = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in mp.values():
                stk.append(c)
            elif c in mp.keys():
                test = stk.pop() if stk else '#'
                if mp[c] != test:
                    return False
        return len(stk) == 0
                