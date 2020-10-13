class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        status = [False] * len(s)
        for word in dict:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    status[i] = True
                start = s.find(word, start+1)
        j = 0
        ans = ""
        while j < len(s):
            if status[j]:
                ans += "<b>"
                while j < len(s) and status[j]:
                    ans += s[j]
                    j += 1
                ans += "</b>"
            else:
                ans += s[j]
                j += 1
        
        return ans