


#
# hi!               -8
#               j.     i   
#         2 5   1.  -4 -3 -5  495  595. 
#
#           1
#    lowest sum that includes input[1] == 3
#
#                                         3
#                                       2 3
#3 2+3


#         2,3   -4, -9 -9, -10, -10, -10  
# for each num, get lowest sum to that point, store indices
# n*2, dp 

from typing import List

def lowestSubSum(nums : List[int]) -> List[int]:
    hm = {}
    
    # dp[i] should be the lowest sum for a range that     ends at and includes i
    l = 0
    minSum = float('inf')
    dpold = nums[0]
    for i in range(1, len(nums)):        
        
        if nums[i] > dpold + nums[i]:
            dp = dpold + nums[i]
            hm[dp] = (l, i)
        else:
            dp = nums[i]
            l = i
                    
        dpold = dp  
        minSum = min(minSum, dp)
        
    return hm[minSum] 
    # capture l at first negative peak
    # capture r at 2nd negative peak
    
input = [ 2,3, -4, -5, 1, -2, 500, 100, -3, -3 ]
#              |   -10     |
#              2           5

print(lowestSubSum(input))

input2 = [ 2,3, -4  , -1,-1,-1,-1,-1,  1, -2, 500, 100, -3, -3 ]
#                |       -10               |
#                2                         9
print ("----------------------")
print(lowestSubSum(input2))


#
# hi!               -8
#               j.     i   
#         2 5   1.  -4 -3 -5  495  595. 
#
#           1
#    lowest sum that includes input[1] == 3
#
#                                         3
#                                       2 3
#3 2+3

from typing import List
#         2,3   -4, -9 -9, -10, -10, -10  
# for each num, get lowest sum to that point, store indices
# n*2, dp 

def lowestSubSum(nums: List[int]) -> List[int]:
    minSoFar = float('inf')
    totalMin = float('inf')
    l = 0
    minCoords = (-1, 0)

    for i in range(0, len(nums)):
        if minSoFar < 0:
            minSoFar += nums[i]
        else:
            minSoFar = nums[i]
            l = i
        
        if totalMin > minSoFar:
            totalMin = minSoFar
            minCoords = l, i

    return minCoords

input = [ 2,3, -4, -5, 1, -2, 500, 100, -3, -3 ]
input2 = [ 2,3, -4, -1,-1,-1,-1,-1,  1, -2, 500, 100, -3, -3 ]

print(lowestSubSum(input) == (2,5))
print(lowestSubSum(input2) == (2,9))
