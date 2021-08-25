def PatternChaser(strParam):
    
    hm = {}

    for i in range(0, len(strParam)-1):
        p = strParam[i]
        for j in range(i+1, len(strParam)):
            p += strParam[j]
            cnt = strParam.count(p)
            if cnt > 1:
                hm[p] = cnt
    
    if len(hm) == 0:
        return "no null"
    
    rtn = sorted(hm, key = lambda x: (-hm[x], -len(x)))[0]
    return f"yes {rtn}"

print(PatternChaser("aa2bbbaacbbb") == "yes bbb")
print(PatternChaser("123224") == "no null")
