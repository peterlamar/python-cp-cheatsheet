"""
7, 2, 5, 10, 8

sum(nums) = 32
best case = 18
m=2

10 + 2 = 12
5 + 7 + 8 = 20

10 + 8 = 18
2 + 5 + 7 = 18

max (18)
min (14)

14 15 16 17 18 19 20
f  f  f. f.  t. t. t

1, 5, 7, 10
sum(nums) = 23
bast case = 12 
m=2

10 + 1 = 11
5 + 7 = 12

1 + 5 = 6
10 + 7 = 17


7, 2, 5, 10, 8

18
7
7+2=9
7+2+5=14<18
14+10>18

10
tF = 2
10+8 = 18


"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def qualified(mid):
            timesFilled = 1
            runningTotal = 0
            for n in nums:
                if runningTotal + n <= mid:
                    runningTotal += n
                else:
                    runningTotal = n
                    timesFilled += 1
            return timesFilled <= m
                    
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if qualified(mid):
                right = mid
            else:
                left = mid + 1
        return left
                