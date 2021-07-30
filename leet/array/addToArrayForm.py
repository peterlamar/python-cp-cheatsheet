class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        for i in range(len(num)-1, -1, -1):
            k = num[i] + k 
            num[i] = k % 10
            k = k // 10
        
        if k:
            num = [int(i) for i in str(k)] + num
        
        return num
            
        