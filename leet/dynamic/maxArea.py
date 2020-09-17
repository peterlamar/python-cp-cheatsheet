class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        leftMax = rightMax = ans = 0
        
        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            if leftMax < rightMax:
                ans = max(ans, leftMax * (r-l))
                l += 1
            else:
                ans = max(ans, rightMax * (r-l))
                r -= 1
                
        return ans