"""
3, 6, 7, 11, H=8
4  4. 4. 4
1  2. 2. 3 sum()=8

34567
FTTTT

[30,11,23,4,20], H = 5

29,30,31
F.  T. T

Input: piles = [3,6,7,11], H = 8
3,6,7,11
3
  6
1 1 

45678
FFTTT


30,11,23,4,20
30
1. 1. 1. 1. 1
5T 

29
2. 1. 1  1. 1
6 F


"""
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def canEatPile(rate):
            hoursFull = 0
            for p in piles:
                # Eat until full
                hoursFull += p // rate
                if p % rate > 0:
                    hoursFull += 1
            return hoursFull <= H
        
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if canEatPile(mid):
                right = mid
            else: 
                left = mid + 1
        return left
                