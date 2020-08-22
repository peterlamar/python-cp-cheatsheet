"""
11 min
"""
def find_corrupt_numbers(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  
  dup = 0 
  missing = 0

  for x, n in enumerate(nums):
    if x+1 != n:
      dup = nums[x]
      missing = x+1

  return [dup, missing]
