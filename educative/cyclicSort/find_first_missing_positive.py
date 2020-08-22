"""
time: 4 min
error:
len(n) not len(nums)
"""

def find_first_missing_positive(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] <= len(nums) and nums[i] > 0 and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1

  for x, n in enumerate(nums):
    if x+1 != n:
      return x+1

  return -1
