import collections
"""
For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""
def commonCharacterCount(s1, s2):
    s1 = collections.Counter(s1)
    s2 = collections.Counter(s2)
    cnt = 0
    for k in s1:
        if k in s2:
            cnt += min(s1[k], s2[k])
    return cnt
    
