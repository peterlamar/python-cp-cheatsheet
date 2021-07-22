class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        rtn = deque()
        maxHeight = float('-inf')
        
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > maxHeight:
                maxHeight = heights[i]
                rtn.appendleft(i)
            
        return rtn