"""
First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".
"""

def lineEncoding(s):
    cnt = 0
    last = s[0]
    rtn = []
    
    for c in s:
        if last != c:
            if cnt > 1:
                rtn.append(str(cnt))
            rtn.append(last)
            last = c
            cnt = 1
        else:
            cnt += 1
    
    if cnt > 1:
        rtn.append(str(cnt))
    rtn.append(last)
        
    return "".join(rtn)
        
from itertools import groupby

def lineEncoding(s):
    rtn = []
    for k,v in groupby(s):
        cnt = len(list(v))
        if cnt > 1:
            rtn.append(str(cnt))
        rtn.append(k)
        
    return "".join(rtn)
        