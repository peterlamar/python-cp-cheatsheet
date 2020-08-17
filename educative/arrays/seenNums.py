# Time Complexity: O(n)
# Space Complexity: O(1)
"""
13 - 4 = 9
13 - (-4) = 17

"""
def two_sum(A, target):
  if len(A) == 0 or len(A) == 1:
    return False

  seenums = {}
  seenums[target - A[0]] = True

  for i in range(1, len(A)):
    if A[i] in seenums:
      return True
    seenums[target - A[i]] = True

  return False

A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum(A,target))