def cyclic_sort(nums):

  for i, n in enumerate(nums):
    j = i 
    target = n
    #Swap numbers
    while j+1 != target:
      nums[j], nums[target-1] = nums[target-1], nums[j] 
      target = nums[j]
      
  return nums
