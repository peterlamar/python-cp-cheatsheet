"""
time: n^2
space: n
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        stk = [(0, [])]
        ans = []

        letters = set(s)
        complete_str = set(''.join(wordDict))
        if len(letters - complete_str) > 0:
            return []
        
        while stk:
            i, path = stk.pop()

            for w in wordDict:
                wend = i + len(w)
                if s[i:wend] == w:
                    if wend == len(s):
                        tmp = " ".join(path + [w])
                        ans.append(tmp)
                    else:
                        stk.append((wend, path + [w]))
        return ans