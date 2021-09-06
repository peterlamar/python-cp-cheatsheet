"""
For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
"""
def arrayChange(inputArray):
        
    rtn = 0
    for i in range(0, len(inputArray)-1):
        if inputArray[i] >= inputArray[i+1]:
            diff = inputArray[i] - inputArray[i+1]
            rtn += diff + 1
            inputArray[i+1] += diff + 1
    return rtn
        