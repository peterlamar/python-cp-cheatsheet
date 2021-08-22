# Problem: we've all seen seven segment displays, like the digits on a digital clock. Seven segments arranged correctly can display the digits 0-9 as well as many other characters. Some examples:
#         _  _
#    ||_||_ |_
#    |  | _| _|

# You can mimic a seven segment in ASCII on a terminal with three rows and columns using underscores and pipes:
# 5: " _ \n|_ \n _|\n"
#  _
# |_
#  _|
# 4: "   \n|_|\n  |\n"
# 1: "   \n|  \n  |\n"
# 
# Pt 1: given a single digit as input, output its seven segment representation
# Restriction: the only inputs are 1, 4, or 5
# Input: 5
# Output:
#  _
# |_
#  _|
# Pt 2: given a number with multiple digits as input, output its seven segment representation
# Input: 1455
# Output:
#         _  _
#    ||_||_ |_
#    |  | _| _|
# 
# Pt 3: given a 3 line string which is the output of part 2, return the number it represents

def getDigitalNum(i : int) -> str:
    digits = {
    1:"   \n|  \n|  \n",
    4:"   \n|_|\n  |\n",
    5:" _ \n|_ \n _|\n"}
    
    return digits[i]

print(getDigitalNum(1) == "   \n|  \n|  \n")
print(getDigitalNum(4) == "   \n|_|\n  |\n")
print(getDigitalNum(5) == " _ \n|_ \n _|\n")

import collections

def getLongDigitalNum(i: int) -> str:
    nums = [int(x) for x in str(i)]
    
    tmp = collections.defaultdict(list)
    
    for n in range(len(nums)):
        myNum = getDigitalNum(nums[n])
        for i, token in enumerate(myNum.split('\n')):
            tmp[i].append(token)
    
    rtn = []
    for k in tmp:
        rtn.append("".join(tmp[k]))
        
    return "\n".join(rtn)

print(getLongDigitalNum(111))
print(getLongDigitalNum(145))
print(getLongDigitalNum(555))

# ' _  _  _ \n|_ |_ |_ \n _| _| _|\n'
from typing import List

def convertDigital( dig : str ) -> int:
    rtn = []
    
    for l in dig:
        tmp = list(l.split('\n'))
        del tmp[3]
        out = []
        print(tmp)
        for i, t in enumerate(zip(*tmp)):
            print(t)

input555 = [' _  _  _ \n|_ |_ |_ \n _| _| _|\n']
input444 = ['         \n|_||_||_|\n  |  |  |\n']
input111 = ['         \n|  |  |  \n|  |  |  \n']

convertDigital( input555 )
