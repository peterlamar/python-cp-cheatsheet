"""
[1,2,3,4,5,6,7,8,9,10], D = 5

12,13,14,15,16,17,18
F  F. F. T  T. T. T

1, 2, 3, 4, 15


def testShip


left = (10) max(weights)
right = (54) sum(weights)

"""

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def testWeights(max, targetDays) -> bool:
            current = 0
            days = 1
            for w in weights:
                # If I have room, add to ship
                if current + w <= max:
                    current += w
                # if ship is full, empty and increment day
                else:
                    current = w
                    days += 1
            return days <= targetDays
        
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if testWeights(mid, D):
                right = mid
            else:
                left = mid + 1
        return left