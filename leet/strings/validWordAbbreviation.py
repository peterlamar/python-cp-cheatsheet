class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        n = '0'
        
        for c in abbr:
            if c.isalpha():
                i += int(n)
                if i >= len(word) or c != word[i]:
                    return False
                i += 1
                n = '0'
            else:
                if n == '0' and c == '0':
                    return False
                n += c
        
        return i + int(n) == len(word)