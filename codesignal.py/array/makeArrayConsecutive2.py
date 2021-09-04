"""
statues = [6, 2, 3, 8]
makeArrayConsecutive2(statues) = 3. (4,5, and 7)
max element - min element - length+1 gets number of
missing elements
"""
def makeArrayConsecutive2(statues):
    
    mn = min(statues)
    mx = max(statues)
    
    return mx - mn - len(statues)+1
