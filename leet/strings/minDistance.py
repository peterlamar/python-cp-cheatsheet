"""
Step 1:
# recursively call self with one character replaced at a time

if not word1 and not word2:
    return 0
if not word1:
    return len(word2)
if not word2:
    return len(word1)
if word1[0] == word2[0]:
    return self.minDistance(word1[1:], word2[1:])
insert = self.minDistance(word1[1:], word2) + 1
delete = self.minDistance(word1, word2[1:]) + 1
edit = self.minDistance(word1[1:], word2[1:]) + 1

return min(insert, delete, edit)

Step 2: (Add Cache)
"""

class Solution:
    def __init__(self):
        self.cache = {}
        
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:],word2[1:])
        if (word1, word2) not in self.cache:
            insert = 1 + self.minDistance(word1,word2[1:])
            delete = 1 + self.minDistance(word1[1:],word2)
            replace = 1 + self.minDistance(word1[1:],word2[1:])
            self.cache[(word1, word2)] = min(insert, delete, replace)
        return self.cache[(word1, word2)]