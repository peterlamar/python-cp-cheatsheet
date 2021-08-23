class Solution:
    """
    https://leetcode.com/problems/fruit-into-baskets/discuss/170740/JavaC%2B%2BPython-Sliding-Window-for-K-Elements
    https://leetcode.com/problems/minimum-size-subarray-sum/
    https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
    https://leetcode.com/problems/max-consecutive-ones-iii/

1. Fill up hash if needed
1. Have a counter or hash-map to count specific array input 
and keep on increasing the window toward right using 
outer loop.
1. Have a while loop inside to reduce the window side by 
sliding toward right. Movement will be based on constraints 
of problem. 
1. Store the current maximum window size or minimum window
size or number of windows based on problem requirement.

    """
    def totalFruit(self, fruits: List[int]) -> int:
        l = rtn = 0
        hm = {}
        
        for r, f in enumerate(fruits):
            
            hm[f] = r
            
            while len(hm) > 2:
                lf = min(hm.values())
                l = max(lf+1, l)
                del hm[fruits[lf]]
                
            rtn = max(rtn, r-l+1)
            
        return rtn