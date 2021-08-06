class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        rtn = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                rtn -= roman[s[i]]
            else:
                rtn += roman[s[i]]
        return rtn + roman[s[-1]]