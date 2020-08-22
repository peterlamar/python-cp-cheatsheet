"""
time: 20 min and 12 min
errors:
off by one: nums[i] <= len(nums) not nums[i] < len(nums)
double loop in 2nd step, flatten logic
"""

def find_first_k_missing_positive(nums, k):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  
  ht = {}
  missingNumbers = []

  for x, n in enumerate(nums):
    if len(missingNumbers) < k:
      if x + 1 != n:
        missingNumbers.append(x+1)
        ht[x+1] = True
    if n > 0:
      ht[n] = True 
  
  z = 1
  while len(missingNumbers) < k:
    if z not in ht:
      missingNumbers.append(z)
    z += 1      
    
  return missingNumbers
