"""
For
picture = ["abc",
           "ded"]
the output should be
addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""
def addBorder(picture):
    b = '*'*(len(picture[0])+2)
    rtn = []
    rtn.append(b)
    for p in picture:
        rtn.append('*'+p+'*')
    rtn.append(b)
    return rtn