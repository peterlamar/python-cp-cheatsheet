"""
For inputString = "00-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
"""
def isMAC48Address(inputString):
    tokens = inputString.split("-")
    
    if len(tokens) != 6:
        return False
    
    for t in tokens:
        if len(t) != 2:
            return False
        if not ("0"<=t[0]<="9" or "A"<=t[0]<="F"):
            return False 
        if not ("0"<=t[1]<="9" or "A"<=t[1]<="F"):
            return False 
    return True
        
