"""
For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.
"""

import collections

def areSimilar(a, b):
    cnt = 0
    
    for a1, b1 in zip(a,b):
        if a1 != b1:
            cnt += 1
    
    if cnt == 0:
        return True 
    
    # Repeated elements, use Counter
    if cnt == 2:
        return collections.Counter(a) == collections.Counter(b)

    return False