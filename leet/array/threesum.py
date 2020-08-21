"""
-1 0 1 2 -1 -4

(-1, 0) : 1
(1, 2) : -3
(2, -1) : -1
(-1, -4) : 5

a + b = -c
c = -a - b

Go through with each pair and test if adding a third number equals a solution

Will produce duplicates

Will sorting fix duplicates?
-4, -1, -1, 0, 1, 2 

  5:-1, 0, 1, 2 
  
  
-4, -1, -1, -1, 0, 1, 2 
Sort and skip over numbers that are the same as the one before

-4, -1, -1, 0, 1, 2 

Errors:
off by one error, 
    while j < len(nums) - 1

Skip duplicates by skipping first duplicate
if i==0 or nums[i] != nums[i-1]:


"""            

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if len(nums) < 3:
            return res
        
        nums.sort()     
   
        i = 0
        while i < len(nums):    
            ht={}
            j = i + 1     
            if i==0 or nums[i] != nums[i-1]:
                while j < len(nums):
                    if nums[j] in ht:
                        res.append([ht[nums [j]][0],ht[nums[j]][1], nums[j]])
                        while j + 1 < len(nums) and nums[j] == nums[j+1]: j += 1

                    compliment = -nums[j] - nums[i]
                    ht[compliment] = [nums[i], nums[j]]
                    j += 1
                    
            i += 1
            
        return res