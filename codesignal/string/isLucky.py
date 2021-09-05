"""
For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
"""
def isLucky(n):
    n = list(str(n))
    l = 0
    r = len(n)-1
    lc = rc = 0
    while l < r:
        lc += int(n[l])
        rc += int(n[r])
        l += 1
        r -= 1
    return lc == rc
        
        

