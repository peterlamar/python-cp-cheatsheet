"""
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
      F.   F.   F. T.   T.   T.  

     if A[mid] >= target:
         true
"""

def find(A, target):

    if len(A) == 0:
        return 0

    def condition(val):
        if A[mid] >= target:
            return True
        else:
            return False
    
    left, right = 0, len(A) - 1
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid 
        else:
            left = mid + 1
    return left

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
x = find(A, target)
print(x)