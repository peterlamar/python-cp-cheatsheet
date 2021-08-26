"""
time: n
space: n
Remove All Adjacent Duplicates in String II
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        
        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
                if stk[-1][1] >= k:
                    stk.pop()
            else:
                stk.append([c, 1])
        
        ans = []
        for c in stk:
            ans.extend([c[0]] * c[1])
        
        return "".join(ans)