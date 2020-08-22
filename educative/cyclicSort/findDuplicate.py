"""
9 min

Error
int i
j = len(nums[i])
"""
def find_duplicate(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[j], nums[i] = nums[i], nums[j]
    else:
      if i != j:
        return nums[i]
      i += 1
  return -1
