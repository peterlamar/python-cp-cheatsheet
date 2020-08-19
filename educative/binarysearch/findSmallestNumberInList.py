"""

1234567
TTTTTTT

0123456
4567123
FFFFTTT

2345671
FFFFFFT

6712345
FFTTTTT

L  M  R
4567123
0123456
   F

LMR
123
456
TTT

"""

def find(A):
  def condition(mid):
    if mid == len(A) - 1:
      return True
    return A[mid] < A[right]

  if len(A) < 2:
    return 0
  
  left, right = 0, len(A) - 1
  while left < right:
    mid = left + (right - left) // 2
    if condition(mid):
      right = mid
    else:
      left = mid + 1

  return left

print(find([4, 5, 6, 7, 1, 2, 3]))