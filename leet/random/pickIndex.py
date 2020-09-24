import random
"""
time: N, pickindex lgn
space: N, 1
"""
class Solution:

    def __init__(self, w: List[int]):
        self.S = sum(w)
        self.picks = []
        total = 0
        for i, weight in enumerate(w):
            total += weight
            self.picks.append(total)
        
            
        

    def pickIndex(self) -> int:
        i = random.randint(1, self.S)
        l, r = 0, len(self.picks)
        
        while l < r:
            m = l + r >> 1
            if self.picks[m] >= i:
                r = m
            else:
                l = m + 1
                
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

import random
"""
time: N, pickindex lgn
space: N, 1
"""
class Solution:

    def __init__(self, w):
        self.w = list(itertools.accumulate(w))

    def pickIndex(self):
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))

        

import random
"""
time: N, pickindex lgn
space: N, 1
"""
class Solution:

    def __init__(self, w):
        self.w = w

    def pickIndex(self):
        return random.choices(range(len(self.w)), weights=self.w)[0]