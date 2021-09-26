"""
For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
"""
def buildPalindrome(st):
    for i in range(len(st)):
        sub = st[i:]
        if sub == sub[::-1]:
            non = st[:i]
            return st + non[::-1]
