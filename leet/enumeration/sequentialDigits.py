class Seqs:
    nums = []
    def __init__(self):
        digits = "123456789"
        N = 10
        for l in range(2, N):
            for s in range(N-l):
                self.nums.append(int(digits[s:s+l]))
        
class Solution:
    s = Seqs()
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        rtn = list()
        candidates = self.s.nums
        for c in candidates:
            if low <= c <= high:
                rtn.append(c)
        return rtn
        