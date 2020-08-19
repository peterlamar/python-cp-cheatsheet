"""
0 k

 k = 26

 0 1 2 3 4 5 6
 F F F F F F T
"""
def integer_square_root(k):
  if k < 2:
    return k

  if k == 2:
    return 1

  left, right = 0, k
  while left < right:
    mid = left + (right - left) // 2
    if mid * mid > k:
      right = mid
    else:
      left = mid + 1

  return left - 1