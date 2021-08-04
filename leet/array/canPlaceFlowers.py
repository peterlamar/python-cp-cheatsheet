class Solution:
    def canPlaceFlowers(self, F: List[int], n: int) -> bool:
        F = [0] + F + [0]
        
        for f in range(1,len(F)-1):
            if F[f-1] == F[f] == F[f+1] == 0:
                F[f] = 1
                n -= 1
        
        return n <= 0