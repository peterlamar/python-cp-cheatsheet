"""
inputArray = ["aba", "aa", "ad", "vcd", "aba"]
allLongestStrings(inputArray) = ["aba", "vcd", "aba"]

"""
def allLongestStrings(inputArray):
    rtn = []
    mxLen = 0
    
    mxLen = len(max(inputArray, key=len))
    for i in inputArray:
        if len(i) == mxLen:
            rtn.append(i)
    
    return rtn

