def find_all_duplicates(nums):
  duplicateNumbers = []

  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      if i != j:
        duplicateNumbers.append(nums[i])
      i += 1

  return duplicateNumbers
