class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter()
        
        for n in nums:
            cnt[n] += 1
        
        twice = none = 0
        for i in range(1, len(nums)+1):
            if cnt[i] == 2:
                twice = i
            
            if cnt[i] == 0:
                none = i
                
        return [twice, none]