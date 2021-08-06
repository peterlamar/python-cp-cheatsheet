https://leetcode.com/problems/buddy-strings/discuss/891275/Python-Best-Simple-and-Clean-Explained-Solution-O(n)-O(1)

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        i = j = 0
        
        if len(s) != len(goal):
            return
        
        if len(s) <= 1:
            return False
        
        if s == goal:
            return True if len(s) - len(set(s)) >= 1 else False
        
        
        s1 = s2 = g1 = g2 = ''
        cnt = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                if cnt == 0:
                    s1 = s[i]
                    g1 = goal[i]
                elif cnt == 1:
                    s2 = s[i]
                    g2 = goal[i]
                elif cnt > 1:
                    return False
                cnt += 1
        
        return (s1 == g2 and g1 == s2 and cnt > 0) 