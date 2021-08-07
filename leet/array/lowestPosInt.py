class Solution:
    def minInteger(self, num: str, k: int) -> str:
        """
    def lowestPosInt1( nums : List[int]) -> int:
        
        nums.sort() #nlogn
        
        for i, n in enumerate(nums): #n
            if i != n:
                return i
        
        return len(nums)
    """

#write a function, input is a list of integers, output the lowest non-negative missing integer

#Ex: [2,3,0,5] -> 1
      
# [1,2,3] -> 0
# [0,1,2,3] -> 4 
# [0, 1000]

def lowestPosInt( nums ) -> int:
    s = set()

    for n in nums:
        s.add(n)

    # 0, 1, 2, 3, 4
    for i in range(len(nums)):
        if i not in s:
            return i
    
    return len(nums)

test1 = [0, 1000]
test2 = [2,3,0,5]
test3 = [-1,-2,-3]
test4 = [0,1,2,3]

print(lowestPosInt(test1) == 1)
print(lowestPosInt(test2) == 1) 
print(lowestPosInt(test3) == 0) 
print(lowestPosInt(test4) == 4) 

